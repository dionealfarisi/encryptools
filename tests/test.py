import unittest
from encryptools import RSAKeyManager, HybridEncryptor, DecryptFileCreator

class TestEncryptools(unittest.TestCase):
    def test_rsa_key_manager(self):
        rsa_manager = RSAKeyManager()
        private_key, public_key = rsa_manager.generate_rsa_keys()
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

    def test_hybrid_encryptor(self):
        rsa_manager = RSAKeyManager()
        hybrid_encryptor = HybridEncryptor()
        private_key, public_key = rsa_manager.generate_rsa_keys()
        
        data = b"Hello, World!"
        encrypted_symmetric_key, iv, ct_bytes = hybrid_encryptor.hybrid_encrypt(data, public_key)
        decrypted_data = hybrid_encryptor.hybrid_decrypt(encrypted_symmetric_key, iv, ct_bytes, private_key)
        
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()