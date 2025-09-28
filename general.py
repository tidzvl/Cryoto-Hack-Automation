from Crypto.Util.number import *

#bytes to big int

s = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

s16 = hex(int(s))
# print(s16)
s_hexbytes = bytes.fromhex(s16[2:] if len(s16) % 2 == 0 else '0' + s16[2:])
# print(s_hexbytes)

from pwn import *
import base64, codecs
from Crypto.Util.number import long_to_bytes
import json

def decode(data):
    t = data['type']
    v = data['encoded']
    if t == 'base64':
        return base64.b64decode(v).decode()
    elif t == 'hex':
        return bytes.fromhex(v).decode()
    elif t == 'rot13':
        return codecs.decode(v, 'rot_13')
    elif t == 'bigint':
        return long_to_bytes(int(v, 16)).decode()
    elif t == 'utf-8':
        return ''.join([chr(c) for c in v])

io = remote('socket.cryptohack.org', 13377)
for _ in range(100):
    data = io.recvuntil(b'}').decode()
    json_data = eval(data)
    decoded = decode(json_data)
    io.sendline(json.dumps({"decoded": decoded}))
    print(f"✅ Solved: {decoded}")

print(io.recvall().decode())
