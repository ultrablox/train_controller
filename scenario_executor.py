from enum import Enum
from datetime import datetime
import logging
from loconet_decoder import *
import time


class OperationState(Enum):
  NOT_STARTED = 0
  RUNNING = 1
  FINISHED = 2

class OperationBase:
  def __init__(self):
    self.__state = OperationState.NOT_STARTED
    self.__startTime = None
  
  def state(self):
    return self.__state

  def start(self, startTime):
    assert self.__state == OperationState.NOT_STARTED
    self.__startTime = startTime
    self.__state = OperationState.RUNNING

  def finish(self):
    assert self.__state == OperationState.RUNNING
    self.__state = OperationState.FINISHED

  def durationSinceStartMs(self, curTime):
    return curTime - self.__startTime

  def run(self, currentTime, dccClient):
    assert False, "Run not implemented"


# Light

class LightState(Enum):
  OFF = 0
  ON = 1

class SwitchLightOperation(OperationBase):
  def __init__(self, state):
    super().__init__()
    self.__state = state

  def run(self, currentTime, dccClient):
    dccClient.send(LNSetLocoDirFunMessage(2, 48 if self.__state == LightState.ON else 32))
    self.finish()


# Change direction

class Direction(Enum):
  FORWARD = 0
  BACKWARD = 1

class SetDirectionOperation(OperationBase):
  def __init__(self, direction):
    super().__init__()
    self.__direction = direction

  def run(self, currentTime, dccClient):
    value = 0 if self.__direction == Direction.FORWARD else 32
    dccClient.send(LNSetLocoDirFunMessage(slot=2, func=value))
    self.finish()

# Wait

class WaitOperation(OperationBase):
  def __init__(self, durationSec):
    super().__init__()
    self.__duration = durationSec * 1e6

  def run(self, currentTime, _):
    if self.durationSinceStartMs(currentTime) > self.__duration:
      self.finish()


# Throttle

class ThrottleOperation(OperationBase):
  def __init__(self, speed):
    super().__init__()
    self.__speed = speed

  def run(self, currentTime, dccClient):
    value = 1 if self.__speed == 0 else 10
    dccClient.send(LNSetLocoSpeedMessage(slot=2, speed=value))
    self.finish()

# Scenario

class ScenarioExecutor:
  def __init__(self, client):
    self.__operations = []
    self.__currentIndex = 0
    self.__client = client

  def switchLight(self, state):
    self.__operations += [ SwitchLightOperation(state) ]

  def setDirection(self, direction):
    self.__operations += [ SetDirectionOperation(direction) ]

  def wait(self, durationSec):
    self.__operations += [ WaitOperation(durationSec) ]
  
  # Real value (0, 1.0]
  def throttle(self, speed):
    self.__operations += [ ThrottleOperation(speed) ]

  def stop(self):
    self.__operations += [ ThrottleOperation(0) ]

  def doWork(self):
    assert self.__currentIndex < len(self.__operations), "Scenario is over"

    currentTime = time.time_ns() // 1000

    curOperation = self.__operations[self.__currentIndex]
    if curOperation.state() == OperationState.NOT_STARTED:
      logging.info('Starting operation {} at {} usec...'.format(curOperation, currentTime))
      curOperation.start(currentTime)

    if curOperation.state() == OperationState.RUNNING:
      curOperation.run(currentTime, self.__client)

    if curOperation.state() == OperationState.FINISHED:
      logging.info('Finished operation {}'.format(curOperation))
      self.__currentIndex = self.__currentIndex + 1
    
