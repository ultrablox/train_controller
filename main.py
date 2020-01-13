#!/usr/bin/env python3
import socket
import binascii
import fcntl, os
import errno
import sys
import select
from loconet_decoder import *
from scenario_executor import *


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

  def run(self):
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

  scenarioRunner = ScenarioExecutor(client)
  scenarioRunner.switchLight(LightState.ON)
  scenarioRunner.setDirection(Direction.FORWARD)
  scenarioRunner.wait(3)
  scenarioRunner.throttle(0.1)
  scenarioRunner.wait(4)
  scenarioRunner.stop()
  scenarioRunner.wait(3)
  scenarioRunner.switchLight(LightState.OFF)

  runner.add(scenarioRunner)
  
  client.connect()
  client.send(LNGlobalPowerOnMessage())

  try:
    runner.run()
  except KeyboardInterrupt:
    client.send(LNGlobalPowerOffMessage())
    sys.exit()


if __name__ == "__main__":
  main()