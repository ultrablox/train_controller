from enum import Enum
from datetime import datetime

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
    dccClient.send(LNSetLocoDirFunMessage(1, 1))
    self.finish()


# Change direction

class Direction(Enum):
  FORWARD = 0
  BACKWARD = 1

class SetDirectionOperation:
  def __init__(self, direction):
    super().__init__()
    self.__direction = direction

  def run(self, currentTime, dccClient):
    # dccClient.send(...)
    self.finish()

# Wait

class WaitOperation:
  def __init__(self, duration):
    super().__init__()
    self.__duration = duration

  def run(self, currentTime, _):
    if self.durationSinceStartMs(currentTime) > self.duration * 1e6:
      self.finish()


# Throttle

class ThrottleOperation:
  def __init__(self, speed):
    super().__init__()
    self.__speed = speed

  def run(self, currentTime, dccClient):
    # dccClient.send(...)
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

  def run(self):
    assert self.__currentIndex < len(self.__operations), "Scenario is over"

    dt = datetime.now()
    currentTime = dt.microsecond

    curOperation = self.__operations[self.__currentIndex]
    if curOperation.state() == OperationState.NOT_STARTED:
      logging.info('Starting operation {}...'.format(curOperation))
      curOperation.start(currentTime)

    if curOperation.state() == OperationState.RUNNING:
      curOperation.run(currentTime, self.__client)

    if curOperation.state() == OperationState.FINISHED:
      logging.info('Finished operation {}'.format(curOperation))
      self.__currentIndex = self.__currentIndex + 1
    
