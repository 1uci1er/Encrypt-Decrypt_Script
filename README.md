# AES Encryption and Decryption Script

This script provides a secure and user-friendly way to encrypt and decrypt text using the **Advanced Encryption Standard (AES)** in **Cipher Feedback (CFB)** mode. It includes a simple menu for users to interact with encryption and decryption functionalities.

---

## Features
1. **Encryption**: Securely encrypt plaintext and save the ciphertext to a file.
2. **Decryption**: Retrieve and decrypt the ciphertext from the file to its original plaintext.
3. **Key Validation**: Ensures the AES key meets the required length (16, 24, or 32 bytes).
4. **Random Initialization Vector (IV)**: A unique IV is generated for each encryption to enhance security.

---

## Workflow

### Encryption Process
1. **Input**: User enters plaintext.
2. **Validation**: The AES key is validated for length.
3. **IV Generation**: A random IV is created.
4. **Cipher Initialization**: AES is set up in CFB mode using the key and IV.
5. **Encryption**: Plaintext is encrypted, and the result is a combination of IV and ciphertext.
6. **Output**: The encrypted data is saved to `encrypted.bin`.

---

### Decryption Process
1. **Input**: The script reads the encrypted file (`encrypted.bin`).
2. **Extract IV**: The IV is extracted from the encrypted data.
3. **Cipher Initialization**: AES is reinitialized using the same key and extracted IV.
4. **Decryption**: The ciphertext is decrypted back to plaintext.
5. **Output**: The original plaintext is displayed.

---

## Menu Diagram

```plaintext
+-----------------------+
|   AES Encryption App  |
+-----------------------+
| 1. Encrypt Text       |
| 2. Decrypt Text       |
| 3. Exit               |
+-----------------------+
