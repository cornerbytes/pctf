from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import random

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(pad(data, AES.block_size))
    return result 

def decrypt(data, key):
    cipher = aes.new(key, AES.MODE_ECB)
    result = cipher.decrypt(data)
    result = unpad(result)
    return result 

def generate_random_key():
    key = list('pahamkak')
    random.shuffle(key)
    key = ''.join(key)
    key = key*2
    return key.encode()

if __name__ == "__main__":
    with open('flag.png', 'rb') as f:
        data = f.read()
    
    first_key = generate_random_key()
    second_key = generate_random_key()
    
    data_enc = encrypt(data=data, key=first_key)
    data_enc = encrypt(data=data_enc, key=second_key)
    
    with open('flag.png.enc', 'wb') as f:
        f.write(data_enc)
