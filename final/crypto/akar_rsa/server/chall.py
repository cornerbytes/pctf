#!/usr/bin/env python3
from Crypto.Util.number import getPrime

try:
    with open("flag.txt", "rb") as f:
        flag = f.read()
except Exception as e:
    print(f"{e}: No flag.txt?")
    exit()

p = getPrime(1024)
q = getPrime(1024)

e = 65537
n = p * q
flag = int.from_bytes(flag, byteorder='big')
c = pow(flag, e, n)


print(f"{n=}")
print(f"{e=}")
print(f"{c=}")
print(f"{p+q=}")

