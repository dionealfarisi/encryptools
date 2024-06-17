import os
import base64
import py_compile

class DecryptFileCreator:
    def create_decrypt_file(self, file_name, iv, ct, enc_sym_key):
        file_name_without_extension = os.path.splitext(file_name)[0]

        decrypt_code = f"""
import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA

def decrypt_file(iv, ct, enc_sym_key, private_key):
    iv_bytes = base64.b64decode(iv)
    ct_bytes = base64.b64decode(ct)
    enc_sym_key_bytes = base64.b64decode(enc_sym_key)

    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    sym_key = cipher_rsa.decrypt(enc_sym_key_bytes)

    cipher = AES.new(sym_key, AES.MODE_CBC, iv_bytes)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt.decode('utf-8')

iv = '{iv}'
ct = '{ct}'
enc_sym_key = '{enc_sym_key}'

private_key_file = "private_key.pem"
if os.path.exists(private_key_file):
    with open(private_key_file, 'rb') as f:
        private_key = f.read()
else:
    private_key = input("Masukkan kunci privat (pem format): ").encode()

decrypted_text = decrypt_file(iv, ct, enc_sym_key, private_key)
exec(decrypted_text)
"""

        decrypt_file_name = file_name_without_extension + ".decrypt.py"
        with open(decrypt_file_name, "w") as f:
            f.write(decrypt_code)

        py_compile.compile(decrypt_file_name, cfile=decrypt_file_name + "c")

        if os.path.exists(decrypt_file_name + "c"):
            os.remove(decrypt_file_name)
            os.rename(decrypt_file_name + "c", decrypt_file_name)