#!/usr/bin/env python3
import socket
import binascii
import fcntl, os
import errno
import sys
import select
from loconet_decoder import *


class DccClient:
  def __init__(self, address, port):
    self.__address = address
    self.__port = port
    self.__socket = None
    self.__decoder = LocoNetDecoder()

  def connect(self):
    logging.info('Connecting to {}:{}'.format(self.__address, self.__port))
    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    self.__socket.connect((self.__address, self.__port))
    self.__socket.setblocking(0)
    logging.info('Connection established')

  def run(self):
    readers, _, _ = select.select(
                  [self.__socket],
                  [],
                  [],
                  0)

    if readers:
      chunk = self.__socket.recv(128)  
      # print('RX: {}'.format(chunk.hex()))
      self.__decoder.process(chunk)

  def send(self, msg):
    data = msg.serialize()
    logging.info('>> {}'.format(msg))
    byteData = bytearray(data)
    self.__socket.send(byteData)


def main():
  # logger = logging.getLogger('train_controller')
  logging.basicConfig(level=logging.INFO)

  client = DccClient('192.168.88.234', 5550)
  client.connect()

  client.send(LNGlobalPowerOnMessage())

  x = 0
  while True:
    try:
      client.run()
    except KeyboardInterrupt:
      client.send(LNGlobalPowerOffMessage())
      sys.exit()


if __name__ == "__main__":
  main()