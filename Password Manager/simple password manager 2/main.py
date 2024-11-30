import os
import base64

# Encode data using Base64
def encode_data(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

# Decode data using Base64
def decode_data(encoded_data):
    return base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')

# Define a simple XOR-based encryption/decryption function for passwords
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

# Read the secret key from the file
def load_key():
    key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret.key")
    with open(key_path, "r") as key_file:
        key = key_file.read()
    return key

# Store the password
def store_password(site, username, password, key):
    encoded_site = encode_data(site)
    encoded_username = encode_data(username)
    encrypted_password = xor_encrypt_decrypt(password, key)

    # Check if the combination of site and username already exists
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as file:
            for line in file:
                stored_site, stored_username, _ = line.strip().split(":")
                if stored_site == encoded_site and stored_username == encoded_username:
                    print("User already has a saved password.")
                    return
    
    with open("passwords.txt", "a") as file:
        file.write(f"{encoded_site}:{encoded_username}:{encrypted_password}\n")
        print("Password stored successfully!")

# Retrieve the password
def retrieve_password(site, username, key):
    if not os.path.exists("passwords.txt"):
        return None
    
    encoded_site = encode_data(site)
    encoded_username = encode_data(username)
    
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_site, stored_username, encrypted_password = line.strip().split(":")
            if stored_site == encoded_site and stored_username == encoded_username:
                return xor_encrypt_decrypt(encrypted_password, key)
    return None

def main():
    # Ensure passwords are stored in the same directory as the script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Load the encryption key from the file
    key = load_key()

    while True:
        choice = input("Do you want to (s)tore or (r)etrieve a password? (q to quit): ")
        if choice == "s":
            site = input("Enter the site name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            store_password(site, username, password, key)
        elif choice == "r":
            site = input("Enter the site name: ")
            username = input("Enter the username: ")
            password = retrieve_password(site, username, key)
            if password:
                print(f"The password for {site} with username {username} is {password}")
            else:
                print(f"No password found for {site} with username {username}")
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please select either 's', 'r', or 'q'.")

if __name__ == "__main__":
    main()
