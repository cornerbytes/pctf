#!/usr/bin/env python3
import zlib

with open("flag", "rb") as f:
    flag = zlib.decompress(f.read())

eval(flag)
