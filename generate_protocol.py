#!/usr/bin/env python3
import json

def generate_message(f, msg):
  msgName = 'LN{}Message'.format(msg['name'])
  f.write('class {}:\n'.format(msgName))
  f.write('  opcode = {}\n'.format(hex(msg['opcode'])))
  f.write('  size = {}\n'.format(msg['size']))
  f.write('  def serialize(self):\n')
  f.write('    res = [ {}.opcode ]\n'.format(msgName))
  f.write('    res += [ loconet_checksum(res) ]\n')
  f.write('    assert len(res) == {}.size, "Invalid serialization"\n'.format(msgName))
  f.write('    return res\n')
  f.write('  def deserialize(self, data):\n')
  f.write('    assert len(data) == {}.size, "Invalid serialization"\n'.format(msgName))
  f.write('  def __str__(self):\n')
  f.write('    return "{}{{}}"\n'.format(msgName))

  f.write('\n\n')
  return msgName

def main():
  inputData = None
  with open('loconet.json', 'r') as f:
    inputData = json.load(f)
  
  messages = inputData['messages']
  
  with open('loconet_messages.py', 'w+') as f:
    f.write('from loconet_utils import *\n\n')

    msgNames = []
    for msg in messages:
      msgNames += [generate_message(f, msg)]
  
    f.write('class LocoNetDecoderBase:\n')
    f.write('  messageClasses = [{}]\n\n'.format(', '.join(msgNames)))


if __name__ == "__main__":
  main()