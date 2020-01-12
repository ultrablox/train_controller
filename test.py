from loconet_decoder import *

def test_opcode_lookup():
  logging.basicConfig(level=logging.DEBUG)
  decoder = LocoNetDecoder()
  decoder.process([0x83, 0x7c]) # Power on
  decoder.process([0x82, 0x7d]) # Power off
  assert False
