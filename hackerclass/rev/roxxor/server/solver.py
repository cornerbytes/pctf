#!/usr/bin/python3 
if __name__ == "__main__":
    with open('output_flag.txt', 'r') as f:
        flag_enc = f.read()
    flag = [chr(ord(i)^13) for i in flag_enc]
    flag = ''.join(flag)
    print(flag)
