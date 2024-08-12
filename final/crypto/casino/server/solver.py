from pwn import *

if __name__ == "__main__":
    p = process('./chall.py')
    # reference : https://marc-stevens.nl/research/md5-1block-collision/
    first_hex = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2'
    second_hex = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2'

    p.sendlineafter(b': ', b'1')
    p.sendlineafter(b': ', first_hex.encode())
    p.sendlineafter(b': ', second_hex.encode())
    print(p.recv().decode())
