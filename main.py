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


class DccClient:
  def __init__(self, address, port):
    self.__address = address
    self.__port = port
    self.__socket = None
    self.__decoder = LocoNetDecoder()
    self.__outQueue = []

  def connect(self):
    logging.info('Connecting to {}:{}'.format(self.__address, self.__port))
    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    self.__socket.connect((self.__address, self.__port))
    self.__socket.setblocking(0)
    logging.info('Connection established')

  def doWork(self):
    readers, writers, _ = select.select(
                  [self.__socket],
                  [self.__socket],
                  [],
                  0)

    if readers:
      chunk = self.__socket.recv(128)
      self.__decoder.process(chunk)

    if writers and self.__outQueue:
      msg = self.__outQueue[0]
      self.__outQueue = self.__outQueue[1:]

      data = msg.serialize()
      logging.info('>> {}'.format(msg))
      byteData = bytearray(data)
      self.__socket.send(byteData)


  def send(self, msg):
    self.__outQueue += [msg]


class ThreadRunner:
  def __init__(self):
    self.__runnables = []

  def add(self, runnable):
    self.__runnables += [runnable]

  def run(self):
    while True:
      for runnable in self.__runnables:
        runnable.doWork()


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

  try:
    runner.run()
  except KeyboardInterrupt:
    pass
    # sys.exit()

  client.send(LNGlobalPowerOffMessage())

if __name__ == "__main__":
  main()