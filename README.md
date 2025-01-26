# Encrypt-Decrypt_Script
AES Encryption and Decryption Script This Python script provides a simple interface for encrypting and decrypting text using the AES (Advanced Encryption Standard) algorithm in CFB (Cipher Feedback) mode. It includes a user-friendly menu with options to:
1.Encrypt Text: Enter plaintext, encrypt it using a secure AES key, and save the encrypted output to a binary file (encrypted.bin).
2.Decrypt Text: Retrieve the encrypted data from the file and decrypt it to restore the original plaintext.
3.Exit the Program: Safely exit the script.
The script ensures secure encryption by generating a random Initialization Vector (IV) for each encryption session. It also validates key lengths to comply with AES standards (16, 24, or 32 bytes). It is useful for beginners learning cryptography or small-scale encryption tasks.
