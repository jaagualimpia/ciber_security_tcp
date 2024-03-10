from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AES_Encrypter:
    def encrypt_aes_cbc(self, key, plaintext):
        iv = b'\x11\xce\xa2"M,t)\x85\xf7\xc6\x99\x90N2S'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return iv + ciphertext

    def decrypt_aes_cbc(self, key, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
        return plaintext.decode()

    # Example usage
    key = b'\x17\xce\xa2"M,t)\x85\xf7\xc6\x99\x90N2S'