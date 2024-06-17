# Encryptools

[![PyPI version](https://badge.fury.io/py/encryptools.svg)](https://badge.fury.io/py/encryptools)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/encryptools.svg)](https://pypi.org/project/encryptools/)

Encryptools is a Python package that provides tools for encrypting and decrypting files using a combination of AES and RSA encryption. This package is designed to simplify the process of securing sensitive data.

## Features

- Generate RSA key pairs
- Encrypt files using AES symmetric encryption
- Encrypt AES keys with RSA for secure key transmission
- Create decryption scripts to easily decrypt the files

## Installation

Encryptools can be installed from PyPI using pip:

```bash
pip install encryptools

## Usage

### Generating RSA Keys

You can generate RSA key pairs using the `RSAKeyManager` class:

```python
from encryptools import RSAKeyManager

rsa_manager = RSAKeyManager()
private_key, public_key = rsa_manager.generate_rsa_keys()

# Save keys to files
rsa_manager.save_rsa_key(private_key, public_key, "private_key.pem", "public_key.pem")
```

### Encrypting Data

Encrypt data using the `HybridEncryptor` class, which combines AES and RSA encryption:

```python
from encryptools import HybridEncryptor

hybrid_encryptor = HybridEncryptor()
data = b"Hello, World!"

# Load public key
with open("public_key.pem", "rb") as f:
    public_key = f.read()

encrypted_symmetric_key, iv, ct_bytes = hybrid_encryptor.hybrid_encrypt(data, public_key)

print("Encrypted symmetric key:", encrypted_symmetric_key)
print("IV:", iv)
print("Ciphertext:", ct_bytes)
```

### Decrypting Data

Decrypt data using the `HybridEncryptor` class:

```python
# Load private key
with open("private_key.pem", "rb") as f:
    private_key = f.read()

decrypted_data = hybrid_encryptor.hybrid_decrypt(encrypted_symmetric_key, iv, ct_bytes, private_key)

print("Decrypted data:", decrypted_data)
```

### Creating Decryption Scripts

Create a decryption script that can be used to decrypt the file later:

```python
from encryptools import DecryptFileCreator

decrypt_file_creator = DecryptFileCreator(symmetric_key)
decrypt_file_creator.write_decrypt_function_to_file("decrypt_script.py", "encrypted_file.bin", "decrypted_file.txt")
```

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repository
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to open an issue or contact me at [ardionefarisi1322@gmail.com](mailto:ardionefarisi1322@gmail.com).

---

Happy encrypting!
```

### Explanation:

1. **Title and Badges**: The title of the package and badges for version, license, and supported Python versions.
2. **Features**: A brief list of what the package can do.
3. **Installation**: Instructions on how to install the package using pip.
4. **Usage**: Detailed code examples on how to generate RSA keys, encrypt data, decrypt data, and create decryption scripts.
5. **Running Tests**: Instructions on how to run tests for the package.
6. **Contributing**: Guidelines for contributing to the project.
7. **License**: Information about the project's license.
8. **Contact**: Contact information for further questions or support.

Feel free to customize the contact information and any other section according to your specific needs.