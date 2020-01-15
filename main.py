#!/usr/bin/env python3
import socket
import binascii
import fcntl, os
import errno
import sys
import select
from loconet_decoder import *
from scenario_executor import *
from locomotive_controller import *
from thread_runner import *
import numpy


class DccClient(Runnable):
  class State(Enum):
    INVALID = -1
    DEFAULT = 0
    WAITING_ECHO = 1
    WAITING_RESPONSE = 2

  def __init__(self, listener, address, port):
    self.__address = address
    self.__port = port
    self.__socket = None
    self.__decoder = LocoNetDecoder()
    self.__outQueue = []
    self.__inQueue = []
    self.__state = self.State.INVALID
    self.__lastSentMsg = None
    self.__listener = listener

  def connect(self):
    logging.info('Connecting to {}:{}'.format(self.__address, self.__port))
    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    self.__socket.connect((self.__address, self.__port))
    self.__socket.setblocking(0)
    logging.info('Connection established')
    self.__state = self.State.DEFAULT

  def doWork(self):
    # Read
    readers, _, _ = select.select(
                  [self.__socket],
                  [],
                  [],
                  0)

    if readers:
      chunk = self.__socket.recv(128)
      self.__inQueue += self.__decoder.process(chunk)

    # Analyze incoming
    while self.__inQueue:
      msg = self.__inQueue[0]
      self.__inQueue = self.__inQueue[1:]

      if self.__state == self.State.WAITING_ECHO:
        if msg.serialize() == self.__lastSentMsg.serialize():
          self.__lastSentMsg = None
          self.__state = self.State.DEFAULT
        else:
          self.dispatch(msg)
      else:
        self.dispatch(msg)

    # Send if possible
    if self.__state == self.State.DEFAULT:
      if self.__outQueue:
        _, writers, _ = select.select(
                    [],
                    [self.__socket],
                    [],
                    0)

        msg = self.__outQueue[0]
        self.__outQueue = self.__outQueue[1:]

        data = msg.serialize()
        logging.info('>> {}'.format(msg))
        byteData = bytearray(data)
        self.__socket.send(byteData)
        self.__lastSentMsg = msg
        self.__state = self.State.WAITING_ECHO
  
  def isFinished(self):
    return False
      

  def send(self, msg):
    self.__outQueue += [msg]

  def dispatch(self, msg):
    logging.info('<< {}'.format(msg))
    self.__listener.onMessageReceived(msg)

  def description(self):
    return 'DccClient'


class DeviceInitializer(Runnable):
  class State(Enum):
    DEFAULT = 0
    POWER_ON_REQUESTED = 1
    SLOT_ALLOCATION_REQUESTED = 2
    FINISHED = 3

  def __init__(self, client):
    self.__client = client
    self.__state = self.State.DEFAULT
    self.__locoSlot = 0

  def doWork(self):
    if self.__state == self.State.DEFAULT:
      self.__client.send(LNGlobalPowerOnMessage())
      self.__state = self.State.POWER_ON_REQUESTED
    if self.__state == self.State.POWER_ON_REQUESTED:
      self.__client.send(LNRequestLocoAddressMessage(0, 3))
      self.__state = self.State.SLOT_ALLOCATION_REQUESTED

  def onMessageReceived(self, msg):
    if self.__state == self.State.SLOT_ALLOCATION_REQUESTED:
      if isinstance(msg, LNReadSlotDataMessage):
        self.__locoSlot = msg.slot()
        self.__state = self.State.FINISHED

  def isFinished(self):
    return self.__state == self.State.FINISHED

  def description(self):
    return 'DeviceInitializer'

  def slot(self):
    return self.__locoSlot

class LayoutController(Runnable):
  class State(Enum):
    DEFAULT = 0
    INITIALIZING = 1
    INITIALIZED = 2
    RUNNING = 3
    FINISHED = 10

  def __init__(self, runner, client):
    self.__runner = runner
    self.__client = client
    self.__state = self.State.DEFAULT

  def isFinished(self):
    return self.__state == self.State.FINISHED

  def description(self):
    return 'LayoutController'

  def doWork(self):
    # print(self.__state)
    if self.__state == self.State.DEFAULT:
      self.__initializer = DeviceInitializer(self.__client)
      self.__runner.add(self.__initializer)
      self.__state = self.State.INITIALIZING
      self.__scenarioRunner = None
    elif self.__state == self.State.INITIALIZING:
      if self.__initializer.isFinished():
        self.__loco = LocomotiveController(self.__client, self.__initializer.slot())
        self.__state = self.State.INITIALIZED
    elif self.__state == self.State.INITIALIZED:
      self.runScenario()
      self.__state = self.State.RUNNING
    elif self.__state == self.State.RUNNING:
      if self.__scenarioRunner.isFinished():
        self.__client.send(LNGlobalPowerOffMessage())
        self.__state = self.State.FINISHED
  
  def runScenario(self):
    sr = ScenarioExecutor(self.__client)
    sr.switchLight(self.__loco, LightState.ON)
    sr.setDirection(self.__loco, Direction.FORWARD)
    sr.wait(2)
    sr.throttle(self.__loco, 0.1)
    sr.wait(1)
    sr.stop(self.__loco)
    sr.wait(1)
    sr.setDirection(self.__loco, Direction.BACKWARD)
    sr.wait(2)
    sr.throttle(self.__loco, 0.1)
    sr.wait(1)
    sr.stop(self.__loco)
    sr.wait(1)
    sr.switchLight(self.__loco, LightState.OFF)

    self.__scenarioRunner = sr
    self.__runner.add(self.__scenarioRunner)


def main():
  # logger = logging.getLogger('train_controller')
  logging.basicConfig(level=logging.INFO)

  runner = ThreadRunner()

  client = DccClient(runner, '192.168.88.234', 5550)
  client.connect()
  runner.add(client)
  
  controller = LayoutController(runner, client)
  runner.add(controller)



  # loco = LocomotiveController(client, 2)



  # runner.add(scenarioRunner)
  
  
  # 
  # client.send(LNGlobalPowerOnMessage())
  # client.send(LNSelectCurrentLocoAddressMessage(6, 98, 0, 3))

  # try:
  runner.run()
  # except KeyboardInterrupt:
  #   pass
    # sys.exit()

  

if __name__ == "__main__":
  main()