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

  def __init__(self, zero = 0, address = 0):
    self.__zero = zero
    self.__address = address

  def serialize(self):
    res = [ LNRequestLocoAddressMessage.opcode ]
    res += [ self.__zero ]
    res += [ self.__address ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestLocoAddressMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestLocoAddressMessage.size, "Invalid deserialization"
    self.__zero = data[1]
    self.__address = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["zero={}".format(self.__zero)]
    paramValues += ["address={}".format(self.__address)]
    return "LNRequestLocoAddressMessage({})".format(", ".join(paramValues))

  def zero(self):
    return self.__zero


  def address(self):
    return self.__address




class LNRequestSwitchAckMessage:
  opcode = 0xbd
  size = 4

  def __init__(self, first = 0, second = 0):
    self.__first = first
    self.__second = second

  def serialize(self):
    res = [ LNRequestSwitchAckMessage.opcode ]
    res += [ self.__first ]
    res += [ self.__second ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSwitchAckMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestSwitchAckMessage.size, "Invalid deserialization"
    self.__first = data[1]
    self.__second = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["first={}".format(self.__first)]
    paramValues += ["second={}".format(self.__second)]
    return "LNRequestSwitchAckMessage({})".format(", ".join(paramValues))

  def first(self):
    return self.__first


  def second(self):
    return self.__second




class LNRequestSwitchStateMessage:
  opcode = 0xbc
  size = 4

  def __init__(self, first = 0, second = 0):
    self.__first = first
    self.__second = second

  def serialize(self):
    res = [ LNRequestSwitchStateMessage.opcode ]
    res += [ self.__first ]
    res += [ self.__second ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSwitchStateMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestSwitchStateMessage.size, "Invalid deserialization"
    self.__first = data[1]
    self.__second = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["first={}".format(self.__first)]
    paramValues += ["second={}".format(self.__second)]
    return "LNRequestSwitchStateMessage({})".format(", ".join(paramValues))

  def first(self):
    return self.__first


  def second(self):
    return self.__second




class LNRequestSlotDataMessage:
  opcode = 0xbb
  size = 4

  def __init__(self, slot = 0, zero = 0):
    self.__slot = slot
    self.__zero = zero

  def serialize(self):
    res = [ LNRequestSlotDataMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__zero ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSlotDataMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestSlotDataMessage.size, "Invalid deserialization"
    self.__slot = data[1]
    self.__zero = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["zero={}".format(self.__zero)]
    return "LNRequestSlotDataMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def zero(self):
    return self.__zero




class LNMoveSlotsMessage:
  opcode = 0xba
  size = 4

  def __init__(self, source = 0, destination = 0):
    self.__source = source
    self.__destination = destination

  def serialize(self):
    res = [ LNMoveSlotsMessage.opcode ]
    res += [ self.__source ]
    res += [ self.__destination ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNMoveSlotsMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNMoveSlotsMessage.size, "Invalid deserialization"
    self.__source = data[1]
    self.__destination = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["source={}".format(self.__source)]
    paramValues += ["destination={}".format(self.__destination)]
    return "LNMoveSlotsMessage({})".format(", ".join(paramValues))

  def source(self):
    return self.__source


  def destination(self):
    return self.__destination




class LNLinkSlotsMessage:
  opcode = 0xb9
  size = 4

  def __init__(self, source = 0, destination = 0):
    self.__source = source
    self.__destination = destination

  def serialize(self):
    res = [ LNLinkSlotsMessage.opcode ]
    res += [ self.__source ]
    res += [ self.__destination ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNLinkSlotsMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNLinkSlotsMessage.size, "Invalid deserialization"
    self.__source = data[1]
    self.__destination = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["source={}".format(self.__source)]
    paramValues += ["destination={}".format(self.__destination)]
    return "LNLinkSlotsMessage({})".format(", ".join(paramValues))

  def source(self):
    return self.__source


  def destination(self):
    return self.__destination




class LNUnlinkSlotsMessage:
  opcode = 0xb8
  size = 4

  def __init__(self, source = 0, destination = 0):
    self.__source = source
    self.__destination = destination

  def serialize(self):
    res = [ LNUnlinkSlotsMessage.opcode ]
    res += [ self.__source ]
    res += [ self.__destination ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNUnlinkSlotsMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNUnlinkSlotsMessage.size, "Invalid deserialization"
    self.__source = data[1]
    self.__destination = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["source={}".format(self.__source)]
    paramValues += ["destination={}".format(self.__destination)]
    return "LNUnlinkSlotsMessage({})".format(", ".join(paramValues))

  def source(self):
    return self.__source


  def destination(self):
    return self.__destination




class LNConsitsFunMessage:
  opcode = 0xb6
  size = 4

  def __init__(self, slot = 0, dirf = 0):
    self.__slot = slot
    self.__dirf = dirf

  def serialize(self):
    res = [ LNConsitsFunMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__dirf ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNConsitsFunMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNConsitsFunMessage.size, "Invalid deserialization"
    self.__slot = data[1]
    self.__dirf = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["dirf={}".format(self.__dirf)]
    return "LNConsitsFunMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def dirf(self):
    return self.__dirf




class LNWriteSlotStatMessage:
  opcode = 0xb5
  size = 4

  def __init__(self, slot = 0, stat = 0):
    self.__slot = slot
    self.__stat = stat

  def serialize(self):
    res = [ LNWriteSlotStatMessage.opcode ]
    res += [ self.__slot ]
    res += [ self.__stat ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNWriteSlotStatMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNWriteSlotStatMessage.size, "Invalid deserialization"
    self.__slot = data[1]
    self.__stat = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["stat={}".format(self.__stat)]
    return "LNWriteSlotStatMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def stat(self):
    return self.__stat




class LNLongAckMessage:
  opcode = 0xb4
  size = 4

  def __init__(self, sentOpcode = 0, response = 0):
    self.__sentOpcode = sentOpcode
    self.__response = response

  def serialize(self):
    res = [ LNLongAckMessage.opcode ]
    res += [ self.__sentOpcode ]
    res += [ self.__response ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNLongAckMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNLongAckMessage.size, "Invalid deserialization"
    self.__sentOpcode = data[1]
    self.__response = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["sentOpcode={}".format(self.__sentOpcode)]
    paramValues += ["response={}".format(self.__response)]
    return "LNLongAckMessage({})".format(", ".join(paramValues))

  def sentOpcode(self):
    return self.__sentOpcode


  def response(self):
    return self.__response




class LNInputStatusMessage:
  opcode = 0xb2
  size = 4

  def __init__(self, address = 0, status = 0):
    self.__address = address
    self.__status = status

  def serialize(self):
    res = [ LNInputStatusMessage.opcode ]
    res += [ self.__address ]
    res += [ self.__status ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNInputStatusMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNInputStatusMessage.size, "Invalid deserialization"
    self.__address = data[1]
    self.__status = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["address={}".format(self.__address)]
    paramValues += ["status={}".format(self.__status)]
    return "LNInputStatusMessage({})".format(", ".join(paramValues))

  def address(self):
    return self.__address


  def status(self):
    return self.__status




class LNSensorStatusMessage:
  opcode = 0xb1
  size = 4

  def __init__(self, address = 0, status = 0):
    self.__address = address
    self.__status = status

  def serialize(self):
    res = [ LNSensorStatusMessage.opcode ]
    res += [ self.__address ]
    res += [ self.__status ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNSensorStatusMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNSensorStatusMessage.size, "Invalid deserialization"
    self.__address = data[1]
    self.__status = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["address={}".format(self.__address)]
    paramValues += ["status={}".format(self.__status)]
    return "LNSensorStatusMessage({})".format(", ".join(paramValues))

  def address(self):
    return self.__address


  def status(self):
    return self.__status




class LNRequestSwitchFunMessage:
  opcode = 0xb0
  size = 4

  def __init__(self, address = 0, status = 0):
    self.__address = address
    self.__status = status

  def serialize(self):
    res = [ LNRequestSwitchFunMessage.opcode ]
    res += [ self.__address ]
    res += [ self.__status ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNRequestSwitchFunMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNRequestSwitchFunMessage.size, "Invalid deserialization"
    self.__address = data[1]
    self.__status = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["address={}".format(self.__address)]
    paramValues += ["status={}".format(self.__status)]
    return "LNRequestSwitchFunMessage({})".format(", ".join(paramValues))

  def address(self):
    return self.__address


  def status(self):
    return self.__status




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
    self.__slot = data[1]
    self.__speed = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["speed={}".format(self.__speed)]
    return "LNSetLocoSpeedMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def speed(self):
    return self.__speed




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
    self.__slot = data[1]
    self.__func = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["func={}".format(self.__func)]
    return "LNSetLocoDirFunMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def func(self):
    return self.__func




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
    self.__slot = data[1]
    self.__func = data[2]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["func={}".format(self.__func)]
    return "LNSetLocoSoundFunMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def func(self):
    return self.__func




class LNReadSlotDataMessage:
  opcode = 0xe7
  size = 14

  def __init__(self, slot = 0, stat = 0, address = 0, speed = 0, direction = 0, track = 0, ss2 = 0, address2 = 0, sound = 0, id1 = 0, id2 = 0):
    self.__slot = slot
    self.__stat = stat
    self.__address = address
    self.__speed = speed
    self.__direction = direction
    self.__track = track
    self.__ss2 = ss2
    self.__address2 = address2
    self.__sound = sound
    self.__id1 = id1
    self.__id2 = id2

  def serialize(self):
    res = [ LNReadSlotDataMessage.opcode ]
    res += [ 14 ]
    res += [ self.__slot ]
    res += [ self.__stat ]
    res += [ self.__address ]
    res += [ self.__speed ]
    res += [ self.__direction ]
    res += [ self.__track ]
    res += [ self.__ss2 ]
    res += [ self.__address2 ]
    res += [ self.__sound ]
    res += [ self.__id1 ]
    res += [ self.__id2 ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNReadSlotDataMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNReadSlotDataMessage.size, "Invalid deserialization"
    assert data[1] == 14, "Invalid variable message size"
    self.__slot = data[2]
    self.__stat = data[3]
    self.__address = data[4]
    self.__speed = data[5]
    self.__direction = data[6]
    self.__track = data[7]
    self.__ss2 = data[8]
    self.__address2 = data[9]
    self.__sound = data[10]
    self.__id1 = data[11]
    self.__id2 = data[12]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["stat={}".format(self.__stat)]
    paramValues += ["address={}".format(self.__address)]
    paramValues += ["speed={}".format(self.__speed)]
    paramValues += ["direction={}".format(self.__direction)]
    paramValues += ["track={}".format(self.__track)]
    paramValues += ["ss2={}".format(self.__ss2)]
    paramValues += ["address2={}".format(self.__address2)]
    paramValues += ["sound={}".format(self.__sound)]
    paramValues += ["id1={}".format(self.__id1)]
    paramValues += ["id2={}".format(self.__id2)]
    return "LNReadSlotDataMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def stat(self):
    return self.__stat


  def address(self):
    return self.__address


  def speed(self):
    return self.__speed


  def direction(self):
    return self.__direction


  def track(self):
    return self.__track


  def ss2(self):
    return self.__ss2


  def address2(self):
    return self.__address2


  def sound(self):
    return self.__sound


  def id1(self):
    return self.__id1


  def id2(self):
    return self.__id2




class LNWriteSlotDataMessage:
  opcode = 0xef
  size = 14

  def __init__(self, slot = 0, stat = 0, address = 0, speed = 0, direction = 0, track = 0, ss2 = 0, address2 = 0, sound = 0, id1 = 0, id2 = 0):
    self.__slot = slot
    self.__stat = stat
    self.__address = address
    self.__speed = speed
    self.__direction = direction
    self.__track = track
    self.__ss2 = ss2
    self.__address2 = address2
    self.__sound = sound
    self.__id1 = id1
    self.__id2 = id2

  def serialize(self):
    res = [ LNWriteSlotDataMessage.opcode ]
    res += [ 14 ]
    res += [ self.__slot ]
    res += [ self.__stat ]
    res += [ self.__address ]
    res += [ self.__speed ]
    res += [ self.__direction ]
    res += [ self.__track ]
    res += [ self.__ss2 ]
    res += [ self.__address2 ]
    res += [ self.__sound ]
    res += [ self.__id1 ]
    res += [ self.__id2 ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNWriteSlotDataMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNWriteSlotDataMessage.size, "Invalid deserialization"
    assert data[1] == 14, "Invalid variable message size"
    self.__slot = data[2]
    self.__stat = data[3]
    self.__address = data[4]
    self.__speed = data[5]
    self.__direction = data[6]
    self.__track = data[7]
    self.__ss2 = data[8]
    self.__address2 = data[9]
    self.__sound = data[10]
    self.__id1 = data[11]
    self.__id2 = data[12]

  def __str__(self):
    paramValues = []
    paramValues += ["slot={}".format(self.__slot)]
    paramValues += ["stat={}".format(self.__stat)]
    paramValues += ["address={}".format(self.__address)]
    paramValues += ["speed={}".format(self.__speed)]
    paramValues += ["direction={}".format(self.__direction)]
    paramValues += ["track={}".format(self.__track)]
    paramValues += ["ss2={}".format(self.__ss2)]
    paramValues += ["address2={}".format(self.__address2)]
    paramValues += ["sound={}".format(self.__sound)]
    paramValues += ["id1={}".format(self.__id1)]
    paramValues += ["id2={}".format(self.__id2)]
    return "LNWriteSlotDataMessage({})".format(", ".join(paramValues))

  def slot(self):
    return self.__slot


  def stat(self):
    return self.__stat


  def address(self):
    return self.__address


  def speed(self):
    return self.__speed


  def direction(self):
    return self.__direction


  def track(self):
    return self.__track


  def ss2(self):
    return self.__ss2


  def address2(self):
    return self.__address2


  def sound(self):
    return self.__sound


  def id1(self):
    return self.__id1


  def id2(self):
    return self.__id2




class LNUnkownMessage:
  opcode = 0xe0
  size = 6

  def __init__(self, one = 0, two = 0, three = 0, address = 0):
    self.__one = one
    self.__two = two
    self.__three = three
    self.__address = address

  def serialize(self):
    res = [ LNUnkownMessage.opcode ]
    res += [ self.__one ]
    res += [ self.__two ]
    res += [ self.__three ]
    res += [ self.__address ]
    res += [ loconet_checksum(res) ]
    assert len(res) == LNUnkownMessage.size, "Invalid serialization"
    return res

  def deserialize(self, data):
    assert loconet_checksum(data[:-1]) == data[-1], "Invalid checksum"
    assert len(data) == LNUnkownMessage.size, "Invalid deserialization"
    self.__one = data[1]
    self.__two = data[2]
    self.__three = data[3]
    self.__address = data[4]

  def __str__(self):
    paramValues = []
    paramValues += ["one={}".format(self.__one)]
    paramValues += ["two={}".format(self.__two)]
    paramValues += ["three={}".format(self.__three)]
    paramValues += ["address={}".format(self.__address)]
    return "LNUnkownMessage({})".format(", ".join(paramValues))

  def one(self):
    return self.__one


  def two(self):
    return self.__two


  def three(self):
    return self.__three


  def address(self):
    return self.__address




class LocoNetDecoderBase:
  messageClasses = [LNBusyMessage, LNGlobalPowerOffMessage, LNGlobalPowerOnMessage, LNIdleMessage, LNRequestLocoAddressMessage, LNRequestSwitchAckMessage, LNRequestSwitchStateMessage, LNRequestSlotDataMessage, LNMoveSlotsMessage, LNLinkSlotsMessage, LNUnlinkSlotsMessage, LNConsitsFunMessage, LNWriteSlotStatMessage, LNLongAckMessage, LNInputStatusMessage, LNSensorStatusMessage, LNRequestSwitchFunMessage, LNSetLocoSpeedMessage, LNSetLocoDirFunMessage, LNSetLocoSoundFunMessage, LNReadSlotDataMessage, LNWriteSlotDataMessage, LNUnkownMessage]

