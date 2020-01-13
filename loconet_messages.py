from loconet_utils import *

class LNBusyMessage:
  opcode = 0x81
  size = 2

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNBusyMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNBusyMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNBusyMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNBusyMessage({})".format(", ".join(paramValues))



class LNGlobalPowerOffMessage:
  opcode = 0x82
  size = 2

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNGlobalPowerOffMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNGlobalPowerOffMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNGlobalPowerOffMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNGlobalPowerOffMessage({})".format(", ".join(paramValues))



class LNGlobalPowerOnMessage:
  opcode = 0x83
  size = 2

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNGlobalPowerOnMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNGlobalPowerOnMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNGlobalPowerOnMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNGlobalPowerOnMessage({})".format(", ".join(paramValues))



class LNIdleMessage:
  opcode = 0x85
  size = 2

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNIdleMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNIdleMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNIdleMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNIdleMessage({})".format(", ".join(paramValues))



class LNRequestLocoAddressMessage:
  opcode = 0xbf
  size = 4

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNRequestLocoAddressMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestLocoAddressMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestLocoAddressMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNRequestLocoAddressMessage({})".format(", ".join(paramValues))



class LNRequestSwitchAckMessage:
  opcode = 0xbd
  size = 4

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNRequestSwitchAckMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSwitchAckMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestSwitchAckMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNRequestSwitchAckMessage({})".format(", ".join(paramValues))



class LNSetLocoSpeedMessage:
  opcode = 0xa0
  size = 4

  def __init__(self, slot = 0, speed = 0):
    self.__slot = slot
    self.__speed = speed

  def serialize(self):
    res = [ LNSetLocoSpeedMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__speed ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoSpeedMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNSetLocoSpeedMessage.size, "Invalid deserialization"
    self.__speed = data[1]
    self.__slot = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["speed={}".format(self.__speed)]
    return "LNSetLocoSpeedMessage({})".format(", ".join(paramValues))



class LNSetLocoDirFunMessage:
  opcode = 0xa1
  size = 4

  def __init__(self, slot = 0, func = 0):
    self.__slot = slot
    self.__func = func

  def serialize(self):
    res = [ LNSetLocoDirFunMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__func ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoDirFunMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNSetLocoDirFunMessage.size, "Invalid deserialization"
    self.__func = data[1]
    self.__slot = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["func={}".format(self.__func)]
    return "LNSetLocoDirFunMessage({})".format(", ".join(paramValues))



class LNSetLocoSoundFunMessage:
  opcode = 0xa2
  size = 4

  def __init__(self, slot = 0, func = 0):
    self.__slot = slot
    self.__func = func

  def serialize(self):
    res = [ LNSetLocoSoundFunMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__func ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSetLocoSoundFunMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNSetLocoSoundFunMessage.size, "Invalid deserialization"
    self.__func = data[1]
    self.__slot = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["func={}".format(self.__func)]
    return "LNSetLocoSoundFunMessage({})".format(", ".join(paramValues))



class LNInputRepMessage:
  opcode = 0xb2
  size = 4

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNInputRepMessage.opcode ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNInputRepMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNInputRepMessage.size, "Invalid deserialization"

  def __str__(self):
    paramValues = []
    return "LNInputRepMessage({})".format(", ".join(paramValues))



class LNReadSlotDataMessage:
  opcode = 0xe7
  size = 14

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNReadSlotDataMessage.opcode ]
    res += [ 14 ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNReadSlotDataMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNReadSlotDataMessage.size, "Invalid deserialization"
    assert data[1] == 14, "Invalid variable message size"

  def __str__(self):
    paramValues = []
    return "LNReadSlotDataMessage({})".format(", ".join(paramValues))



class LNWriteSlotDataMessage:
  opcode = 0xef
  size = 14

  def __init__(self):
    pass

  def serialize(self):
    res = [ LNWriteSlotDataMessage.opcode ]
    res += [ 14 ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNWriteSlotDataMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNWriteSlotDataMessage.size, "Invalid deserialization"
    assert data[1] == 14, "Invalid variable message size"

  def __str__(self):
    paramValues = []
    return "LNWriteSlotDataMessage({})".format(", ".join(paramValues))



class LocoNetDecoderBase:
  messageClasses = [LNBusyMessage, LNGlobalPowerOffMessage, LNGlobalPowerOnMessage, LNIdleMessage, LNRequestLocoAddressMessage, LNRequestSwitchAckMessage, LNSetLocoSpeedMessage, LNSetLocoDirFunMessage, LNSetLocoSoundFunMessage, LNInputRepMessage, LNReadSlotDataMessage, LNWriteSlotDataMessage]

