#!/bin/sh
FLAG=`cat flag.txt`
qrcode -t "${FLAG}" | xargs -I {} python3 -c 'print("{}".replace("█","。"))'
