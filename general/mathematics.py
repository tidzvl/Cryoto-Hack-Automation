#
# File: mathematics.py
# Author: TiDz
# Contact: nguyentinvs123@gmail.com
# Created on Sun Sep 28 2025
# Description: 
# Useage: 
#

#gnd calcu at "https://www.alcula.com/calculators/math/gcd/#gsc.tab=0"

# or

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
# print("gcd:", gcd)
# print("u:", u)
# print("v:", v)
# print("Flag:", min(u, v))

