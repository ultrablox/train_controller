from loconet_utils import *

class LNBusyMessage:
  opcode = 0x81
  size = 2
  def serialize(self):
    res = [ LNBusyMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNBusyMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNBusyMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNBusyMessage"


class LNGlobalPowerOffMessage:
  opcode = 0x82
  size = 2
  def serialize(self):
    res = [ LNGlobalPowerOffMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNGlobalPowerOffMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNGlobalPowerOffMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNGlobalPowerOffMessage"


class LNGlobalPowerOnMessage:
  opcode = 0x83
  size = 2
  def serialize(self):
    res = [ LNGlobalPowerOnMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNGlobalPowerOnMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNGlobalPowerOnMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNGlobalPowerOnMessage"


class LNIdleMessage:
  opcode = 0x85
  size = 2
  def serialize(self):
    res = [ LNIdleMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNIdleMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNIdleMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNIdleMessage"


class LNRequestLocoAddressMessage:
  opcode = 0xbf
  size = 4
  def serialize(self):
    res = [ LNRequestLocoAddressMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestLocoAddressMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNRequestLocoAddressMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNRequestLocoAddressMessage"


class LNRequestSwitchAckMessage:
  opcode = 0xbd
  size = 4
  def serialize(self):
    res = [ LNRequestSwitchAckMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSwitchAckMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNRequestSwitchAckMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNRequestSwitchAckMessage"


class LNSetLocoSpeedMessage:
  opcode = 0xa0
  size = 4
  def serialize(self):
    res = [ LNSetLocoSpeedMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoSpeedMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNSetLocoSpeedMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNSetLocoSpeedMessage"


class LNSetLocoDirFunMessage:
  opcode = 0xa1
  size = 4
  def serialize(self):
    res = [ LNSetLocoDirFunMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoDirFunMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNSetLocoDirFunMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNSetLocoDirFunMessage"


class LNSetLocoSoundFunMessage:
  opcode = 0xa2
  size = 4
  def serialize(self):
    res = [ LNSetLocoSoundFunMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoSoundFunMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNSetLocoSoundFunMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNSetLocoSoundFunMessage"


class LNInputRepMessage:
  opcode = 0xb2
  size = 4
  def serialize(self):
    res = [ LNInputRepMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNInputRepMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNInputRepMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNInputRepMessage"


class LNReadSlotDataMessage:
  opcode = 0xe7
  size = 14
  def serialize(self):
    res = [ LNReadSlotDataMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNReadSlotDataMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNReadSlotDataMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNReadSlotDataMessage"


class LNWriteSlotDataMessage:
  opcode = 0xef
  size = 14
  def serialize(self):
    res = [ LNWriteSlotDataMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNWriteSlotDataMessage.size, "Invalid serialization"
    return res
  def deserialize(self, data):
    assert len(data) == LNWriteSlotDataMessage.size, "Invalid serialization"
  def __str__(self):
    return "LNWriteSlotDataMessage"


class LocoNetDecoderBase:
  messageClasses = [LNBusyMessage, LNGlobalPowerOffMessage, LNGlobalPowerOnMessage, LNIdleMessage, LNRequestLocoAddressMessage, LNRequestSwitchAckMessage, LNSetLocoSpeedMessage, LNSetLocoDirFunMessage, LNSetLocoSoundFunMessage, LNInputRepMessage, LNReadSlotDataMessage, LNWriteSlotDataMessage]

