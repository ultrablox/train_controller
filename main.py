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
import numpy


class DccClient:
  class State(Enum):
    INVALID = -1
    DEFAULT = 0
    WAITING_ECHO = 1
    WAITING_RESPONSE = 2

  def __init__(self, address, port):
    self.__address = address
    self.__port = port
    self.__socket = None
    self.__decoder = LocoNetDecoder()
    self.__outQueue = []
    self.__inQueue = []
    self.__state = self.State.INVALID
    self.__lastSentMsg = None

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

    return False
      

  def send(self, msg):
    self.__outQueue += [msg]

  def dispatch(self, msg):
    logging.info('<< {}'.format(msg))

  def description(self):
    return 'DccClient'


class ThreadRunner:
  def __init__(self):
    self.__runnables = []

  def add(self, runnable):
    self.__runnables += [runnable]

  def run(self):
    while True:
      for runnable in self.__runnables:
        finished = runnable.doWork()
        if finished:
          logging.info('Runnable "{}" is finished'.format(runnable.description()))
          self.__runnables.remove(runnable)


def main():
  # logger = logging.getLogger('train_controller')
  logging.basicConfig(level=logging.INFO)

  runner = ThreadRunner()

  client = DccClient('192.168.88.234', 5550)
  runner.add(client)

  loco = LocomotiveController(client, 2)

  scenarioRunner = ScenarioExecutor(client)
  scenarioRunner.switchLight(loco, LightState.ON)
  scenarioRunner.setDirection(loco, Direction.FORWARD)
  scenarioRunner.wait(3)
  scenarioRunner.throttle(loco, 0.1)
  scenarioRunner.wait(1)
  scenarioRunner.stop(loco)
  scenarioRunner.wait(3)
  scenarioRunner.setDirection(loco, Direction.BACKWARD)
  scenarioRunner.wait(3)
  scenarioRunner.throttle(loco, 0.1)
  scenarioRunner.wait(1)
  scenarioRunner.stop(loco)
  scenarioRunner.wait(2)
  scenarioRunner.switchLight(loco, LightState.OFF)
  scenarioRunner.wait(2)

  runner.add(scenarioRunner)
  
  client.connect()
  # client.send(LNRequestLocoAddressMessage(0, 3))
  client.send(LNGlobalPowerOnMessage())
  # client.send(LNSelectCurrentLocoAddressMessage(6, 98, 0, 3))

  # try:
  runner.run()
  # except KeyboardInterrupt:
  #   pass
    # sys.exit()

  client.send(LNGlobalPowerOffMessage())

if __name__ == "__main__":
  main()