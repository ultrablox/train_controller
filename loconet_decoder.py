import logging
from loconet_messages import *

class LocoNetDecoder(LocoNetDecoderBase):
  def __init__(self):
    self.__opcodeMessages = {}
    for msgClass in LocoNetDecoderBase.messageClasses:
      self.__opcodeMessages[msgClass.opcode] = msgClass
    self.__buffer = []

  def process(self, chunk):
    self.__buffer += chunk

    while self.__tryProcess():
      pass

  def __tryProcess(self):
    if len(self.__buffer) == 0:
      return False

    logging.debug('Current buffer: {}'.format(self.__buffer))
        
    opcode = self.__buffer[0]
    msgClass = self.__opcodeMessages[opcode]

    assert msgClass, 'No message found for opcode {}'.format(opcode)
    msgLen = msgClass.size

    if len(self.__buffer) < msgLen:
      return False

    logging.debug('Found message of class: {} {} bytes len'.format(msgClass, msgLen))
    msg = msgClass()
    msg.deserialize(self.__buffer[0:msgLen])

    logging.info("<< {}".format(msg))

  
    self.__buffer = self.__buffer[msgLen:]

    return True
