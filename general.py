from Crypto.Util.number import *

#bytes to big int

s = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

s16 = hex(int(s))
# print(s16)
s_hexbytes = bytes.fromhex(s16[2:] if len(s16) % 2 == 0 else '0' + s16[2:])
print(s_hexbytes)