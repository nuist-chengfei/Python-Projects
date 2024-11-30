import os
import string
import random

# Generate a random key for encryption/decryption and save it into a file
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret.key")
    with open(key_path, "w") as key_file:
        key_file.write(key)

# Run this function once to create the secret.key file
if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret.key")):
    generate_key()
