from Crypto.PublicKey import RSA

class RSAKeyManager:
    def __init__(self, key_size=2048):
        self.key_size = key_size

    def generate_keys(self):
        key = RSA.generate(self.key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    def save_key(self, key, file_path):
        with open(file_path, 'wb') as f:
            f.write(key)

    def load_key(self, file_path):
        with open(file_path, 'rb') as f:
            return RSA.import_key(f.read())