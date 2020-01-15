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

    res = []
    while True:
      parsedMsg = self.__tryProcess()
      if parsedMsg:
        res += [parsedMsg]
      else:
        break
    return res

  def __tryProcess(self):
    if len(self.__buffer) == 0:
      return None

    logging.debug('Current buffer: {}'.format(list(map(lambda x: hex(x), self.__buffer))))
        
    opcode = self.__buffer[0]
    msgClass = self.__opcodeMessages[opcode]

    assert msgClass, 'No message found for opcode {}'.format(opcode)
    msgLen = msgClass.size

    if len(self.__buffer) < msgLen:
      return None

    logging.debug('Found message of class: {} {} bytes len'.format(msgClass, msgLen))
    msg = msgClass()
    msg.deserialize(self.__buffer[0:msgLen])

    self.__buffer = self.__buffer[msgLen:]

    return msg
