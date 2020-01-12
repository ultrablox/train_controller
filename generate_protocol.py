#!/usr/bin/env python3
import json

class MessageGenerator:
  def __init__(self, file, jnode):
    self.__file = file
    self.__node = jnode
    self.__className = 'LN{}Message'.format(self.__node['name'])
    self.__size = self.__node['size']
    self.__opcode = self.__node['opcode']
    self.__fields = self.__node['fields'] if 'fields' in self.__node else []

  def generate(self):
    self.__write('class {}:\n'.format(self.__className))
    self.__write('  opcode = {}\n'.format(hex(self.__opcode)))
    self.__write('  size = {}\n'.format(self.__size))
    self.__write('\n')

    # Constructor
    paramNames = ['self'] + list(map(lambda x: '{} = 0'.format(x['name']), self.__fields))
    self.__write('  def __init__({}):\n'.format(', '.join(paramNames)))
    if self.__fields:
      for field in self.__fields:
        self.__write('    self.__{} = {}\n'.format(field['name'], field['name']))
    else:
      self.__write('    pass\n')
    self.__write('\n')
  

    # Serialization
    self.__write('  def serialize(self):\n')
    self.__write('    res = [ {}.opcode ]\n'.format(self.__className))
    self.__write('    res += [ loconet_checksum(res) ]\n')
    self.__write('    assert len(res) == {}.size, "Invalid serialization"\n'.format(self.__className))
    self.__write('    return res\n')
    self.__write('\n')

    # Deserialization
    self.__write('  def deserialize(self, data):\n')
    self.__write('    assert len(data) == {}.size, "Invalid serialization"\n'.format(self.__className))
    self.__write('\n')

    # Stringify
    self.__write('  def __str__(self):\n')
    self.__write('    paramValues = []\n')
    for field in self.__fields:
      self.__write('    paramValues += ["')
      self.__write('{}={{}}'.format(field['name']))
      self.__write('".format(self.__{})]\n'.format(field['name']))
        
    self.__write('    return "{}('.format(self.__className))
    self.__write('{}')
    # }}".format("Xxxxx")\n'.format())
    self.__write(')".format(", ".join(paramValues))\n')

     
    self.__write('\n')

    self.__write('\n\n')
    return self.__className

  def __write(self, line):
    self.__file.write(line)



def main():
  inputData = None
  with open('loconet.json', 'r') as f:
    inputData = json.load(f)
  
  messages = inputData['messages']
  
  with open('loconet_messages.py', 'w+') as f:
    f.write('from loconet_utils import *\n\n')

    msgNames = []
    for msg in messages:
      msgGen = MessageGenerator(f, msg)
      msgNames += [msgGen.generate()]
  
    f.write('class LocoNetDecoderBase:\n')
    f.write('  messageClasses = [{}]\n\n'.format(', '.join(msgNames)))


if __name__ == "__main__":
  main()