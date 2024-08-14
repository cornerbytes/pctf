from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import random

def encrypt(data, key):
    #remove pad
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(data)
    return result 

def decrypt(data, key):
    # remove unpad
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.decrypt(data)
    return result 

def generate_random_key():
    key = list('pahamkak')
    random.shuffle(key)
    key = ''.join(key)
    key = key*2
    return key.encode()


def decrypt2(data, key):
    # add unpad 
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.decrypt(data)
    result = unpad(result, AES.block_size)
    return result

if __name__ == "__main__":
    key_list = list()
    for i in range(10000): 
        key_list.append(generate_random_key())
    key_list = list(set(key_list)) # filter duplicate key
    print(f'possiblity key : {len(key_list)}')

    # known plaintext because 16 bytes of png always the same 
    # and aes operate(encrypt or decrypt) in 128 bit block 
    known_plain_text = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
    first_block = dict()
    for i in key_list:
        result = encrypt(data=known_plain_text, key=i)
        first_block[result] = i 

    with open('flag.png.enc', 'rb') as f:
        known_cipher_text = f.read()

    second_block = dict()
    for i in key_list:
        result = decrypt(data=known_cipher_text, key=i)
        result = result[:16]
        second_block[result] = i 

    ## find the intersection of two block 
    x = set(first_block)
    y = set(second_block)
    z = x.intersection(y)
    z = list(z)[0]
    first_key = first_block[z]
    second_key = second_block[z]
    assert len(first_key) == len(second_key) # raise an error if key not found
    print(f"first_key: {first_key}\nsecond_key : {second_key}")

    known_cipher_text = decrypt2(data=known_cipher_text, key=second_key)
    known_cipher_text = decrypt2(data=known_cipher_text, key=first_key)

    with open('flag_fix.png', 'wb') as f:
        f.write(known_cipher_text)
