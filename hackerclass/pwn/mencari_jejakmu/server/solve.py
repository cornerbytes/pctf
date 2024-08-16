#!/usr/bin/env python3
import subprocess
import re

cmd = "ltrace -s 100 ./chall"
data = subprocess.run(cmd, input=b"asal", shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
pattern = b"PCTF{.*}"
regex = re.compile(pattern)

print(regex.findall(data)[0].decode())
