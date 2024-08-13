#!/usr/bin/env python3
import zlib
import os

FLAG = os.environ["FLAG"]
with open("flag", "wb") as f, open("flag.txt","w") as plain_flag:
    f.write(zlib.compress(f"print(\"{FLAG}\")".encode()))
    plain_flag.write(FLAG)
