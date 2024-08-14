#!/usr/bin/env python3
import subprocess
import os, tempfile

qrcode = subprocess.run("./script.sh", shell=True, stdout=subprocess.PIPE).stdout
qrcode = qrcode.replace("。".encode(),"█".encode())

tmpfd, tmpfpath = tempfile.mkstemp()
try:
    with open(tmpfd,"wb") as f:
        f.write(qrcode)
finally:
    image = subprocess.run(f"""/usr/bin/convert -gravity center -pointsize 3 -background black \
                               -fill white -size 720x720 -font /usr/share/fonts/opentype/freefont/FreeMono.otf \
                               caption:@{tmpfpath} png:-""", shell=True, stdout=subprocess.PIPE).stdout
    os.remove(tmpfpath)
tmpfd, tmpfpath = tempfile.mkstemp()

try:
    with open(tmpfd,"wb") as f:
        f.write(image)
finally:
    flag = subprocess.run(f"grcode {tmpfpath}", shell=True, stdout=subprocess.PIPE).stdout.decode()
    print(flag)
    os.remove(tmpfpath)

