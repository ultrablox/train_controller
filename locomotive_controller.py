from aenum import *
from scenario_executor import *

class LocomotiveController:
  class DirFunBits(IntEnum):
    DIR = 4
    LIGHT = 5

  def __init__(self, dccClient, slotNumber):
    self.__client = dccClient
    self.__slot = slotNumber
    self.__dirFunState = [0, 0, 0, 0, 0, 0, 0, 0]
  
  def __updateDirFunsByte(self):
    self.__client.send(LNSetLocoDirFunMessage(slot=self.__slot, func=self.__byteFromBits(self.__dirFunState)))

  def __byteFromBits(self, bits):
    res = 0
    for i in range(0, 8):
      if bits[i]:
        res = res | (1 << i)
    return res

  def switchLight(self, lightState):
    value = 1 if lightState == LightState.ON else 0
    self.__dirFunState[self.DirFunBits.DIR] = value
    self.__updateDirFunsByte()
    

  def setDirection(self, direction):
    value = 0 if direction == Direction.FORWARD else 1
    self.__dirFunState[self.DirFunBits.LIGHT] = value
    self.__updateDirFunsByte()

  def setSpeed(self, speed):
    value = 1 if speed == 0 else 10
    self.__client.send(LNSetLocoSpeedMessage(slot=self.__slot, speed=value))
