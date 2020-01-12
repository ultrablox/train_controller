
def loconet_checksum(data):
  res = 0xff
  for byte in data:
    res = res ^ byte
  return res
