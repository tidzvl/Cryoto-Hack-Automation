from pwn import *

s = "label"
#xor to 13
enc = ''.join([chr(ord(c) ^ 13) for c in s])
# print(enc)

from Crypto.Util.number import bytes_to_long, long_to_bytes

def xor_hex(a, b):
    return hex(int(a, 16) ^ int(b, 16))[2:].zfill(len(a))

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_ALL = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY2 = xor_hex(KEY2_XOR_KEY1, KEY1)
KEY3 = xor_hex(KEY2_XOR_KEY3, KEY2)

ALL_KEYS = xor_hex(xor_hex(KEY1, KEY2), KEY3)
FLAG = xor_hex(FLAG_XOR_ALL, ALL_KEYS)

# print("crypto{" + bytes.fromhex(FLAG).decode() + "}")

cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytes.fromhex(cipher_hex)

# for key in range(256):
#     decoded = ''.join([chr(b ^ key) for b in cipher_bytes])
#     if "crypto" in decoded:
#         print(f"Key: {key}, Flag: crypto{{{decoded}}}")
#         break

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytes.fromhex(cipher_hex)

cipher = bytes.fromhex(cipher_hex)
key = xor(cipher[:7], b"crypto{") + xor(cipher[-1:], b"}")
full_key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]

flag = xor(cipher, full_key)
# print(flag.decode())

from PIL import Image

img1 = Image.open("../code_base/1.png")
img2 = Image.open("../code_base/2.png")

result = Image.new("RGB", img1.size)

for x in range(img1.width):
    for y in range(img1.height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        xor_pixel = tuple([a ^ b for a, b in zip(pixel1, pixel2)])
        result.putpixel((x, y), xor_pixel)

result.save("xor_result.png")

