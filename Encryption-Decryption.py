from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import b2a_hex, a2b_hex

# Author: Solanki Aditya
# Date: 14/03/2024
# Description: A script for encrypting and decrypting text using AES in CFB mode.
# Requirements:
# Install pycryptodome library using: pip install pycryptodome

# Ensure the key length is valid (16, 24, or 32 bytes for AES)
def validate_key(key):
    if len(key) not in {16, 24, 32}:
        raise ValueError("Key length must be 16, 24, or 32 bytes.")
    return key


# Encrypt the plaintext using AES
def encrypt(plain_text, key):
    try:
        validate_key(key)

        # Generate a random IV (initialization vector)
        iv = get_random_bytes(AES.block_size)

        # Create AES cipher object in CFB mode
        cipher = AES.new(key, AES.MODE_CFB, iv)

        # Encrypt the plaintext
        ciphertext = cipher.encrypt(plain_text.encode())

        # Return IV + ciphertext as the final encrypted message
        return iv + ciphertext

    except Exception as e:
        print(f"Encryption error: {e}")
        return None


# Decrypt the ciphertext using AES
def decrypt(ciphertext, key):
    try:
        validate_key(key)

        # Extract the IV from the beginning of the ciphertext
        iv = ciphertext[:AES.block_size]

        # Extract the actual ciphertext
        actual_ciphertext = ciphertext[AES.block_size:]

        # Create AES cipher object in CFB mode using the same key and IV
        cipher = AES.new(key, AES.MODE_CFB, iv)

        # Decrypt the ciphertext
        decrypted_text = cipher.decrypt(actual_ciphertext)
        return decrypted_text.decode()

    except Exception as e:
        print(f"Decryption error: {e}")
        return None


if __name__ == "__main__":
    key = b'thekeyisnothingsetnowbut'  # Define a key (16 bytes for AES-128)

    while True:
        print("\nMenu:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            plain_text = input("Enter text to encrypt: ")
            encrypted_data = encrypt(plain_text, key)
            if encrypted_data:
                print("Encrypted data (hex):", b2a_hex(encrypted_data).decode())
                with open("encrypted.bin", "wb") as file_out:
                    file_out.write(encrypted_data)
        elif choice == "2":
            try:
                with open("encrypted.bin", "rb") as file_in:
                    encrypted_data = file_in.read()
                decrypted_data = decrypt(encrypted_data, key)
                if decrypted_data:
                    print("Decrypted data:", decrypted_data)
            except FileNotFoundError:
                print("Error: No encrypted file found.")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")
