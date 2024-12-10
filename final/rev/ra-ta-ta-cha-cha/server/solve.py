from Crypto.Cipher import ChaCha20
if __name__ == "__main__":
    
    # using 12 static bytes from png file
    nonce = bytes([137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13])
    key = bytes([15, 188, 195, 48, 183, 191, 111, 36, 240, 221, 172, 20, 60, 201, 58, 239, 91, 18, 205, 93, 70, 134, 155, 176, 76, 66, 248, 199, 123, 204, 68, 208])
    cipher = ChaCha20.new(key=key, nonce=nonce)
    with open('flag.png.bean', 'rb') as f:
        ciphertext = f.read()

    with open('flag.png', 'wb') as flag:
        flag.write(cipher.decrypt(ciphertext))

