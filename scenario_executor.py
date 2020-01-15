from enum import Enum
from datetime import datetime
import logging
from loconet_decoder import *
import time
from thread_runner import *


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

  def run(self, currentTime):
    assert False, "Run not implemented"


# Light

class LightState(Enum):
  OFF = 0
  ON = 1

class SwitchLightOperation(OperationBase):
  def __init__(self, loco, state):
    super().__init__()
    self.__state = state
    self.__locoController = loco

  def run(self, currentTime):
    self.__locoController.switchLight(self.__state)
    self.finish()


# Change direction

class Direction(Enum):
  FORWARD = 0
  BACKWARD = 1

class SetDirectionOperation(OperationBase):
  def __init__(self, loco, direction):
    super().__init__()
    self.__direction = direction
    self.__locoController = loco

  def run(self, currentTime):
    self.__locoController.setDirection(self.__direction)
    self.finish()

# Wait

class WaitOperation(OperationBase):
  def __init__(self, durationSec):
    super().__init__()
    self.__duration = durationSec * 1e6

  def run(self, currentTime):
    if self.durationSinceStartMs(currentTime) > self.__duration:
      self.finish()


# Throttle

class ThrottleOperation(OperationBase):
  def __init__(self, loco, speed):
    super().__init__()
    self.__speed = speed
    self.__locoController = loco

  def run(self, currentTime):
    self.__locoController.setSpeed(self.__speed)
    self.finish()

# Scenario

class ScenarioExecutor(Runnable):
  def __init__(self, client):
    self.__operations = []
    self.__currentIndex = 0
    self.__client = client

  def switchLight(self, loco, state):
    self.__operations += [ SwitchLightOperation(loco, state) ]

  def setDirection(self, loco, direction):
    self.__operations += [ SetDirectionOperation(loco, direction) ]

  def wait(self, durationSec):
    self.__operations += [ WaitOperation(durationSec) ]
  
  # Real value (0, 1.0]
  def throttle(self, loco, speed):
    self.__operations += [ ThrottleOperation(loco, speed) ]

  def stop(self, loco):
    self.__operations += [ ThrottleOperation(loco, 0) ]
  
  def description(self):
    return 'ScenarioExecutor'

  def doWork(self):
    assert self.__currentIndex < len(self.__operations)

    currentTime = time.time_ns() // 1000

    curOperation = self.__operations[self.__currentIndex]
    if curOperation.state() == OperationState.NOT_STARTED:
      logging.info('Starting operation {} at {} usec...'.format(curOperation, currentTime))
      curOperation.start(currentTime)

    if curOperation.state() == OperationState.RUNNING:
      curOperation.run(currentTime)

    if curOperation.state() == OperationState.FINISHED:
      logging.info('Finished operation {}'.format(curOperation))
      self.__currentIndex = self.__currentIndex + 1

  def isFinished(self):
    return self.__currentIndex == len(self.__operations)
    
