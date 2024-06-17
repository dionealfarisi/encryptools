from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA  # Tambahkan impor ini
from Crypto.Random import get_random_bytes
import base64

class HybridEncryptor:
    def __init__(self, aes_key_size=16):
        self.aes_key_size = aes_key_size

    def generate_symmetric_key(self):
        return get_random_bytes(self.aes_key_size)

    def encrypt_data(self, data, symmetric_key):
        cipher = AES.new(symmetric_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def encrypt_symmetric_key(self, symmetric_key, public_key):
        rsa_key = RSA.import_key(public_key)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        enc_sym_key = cipher_rsa.encrypt(symmetric_key)
        return base64.b64encode(enc_sym_key).decode('utf-8')

    def decrypt_data(self, iv, ct, symmetric_key):
        iv_bytes = base64.b64decode(iv)
        ct_bytes = base64.b64decode(ct)
        cipher = AES.new(symmetric_key, AES.MODE_CBC, iv_bytes)
        pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
        return pt.decode('utf-8')

    def decrypt_symmetric_key(self, enc_sym_key, private_key):
        enc_sym_key_bytes = base64.b64decode(enc_sym_key)
        rsa_key = RSA.import_key(private_key)
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        return cipher_rsa.decrypt(enc_sym_key_bytes)