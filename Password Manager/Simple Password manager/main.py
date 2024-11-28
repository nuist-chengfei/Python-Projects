import base64
import os

# Encode a password
def encode_password(password):
    password_bytes = password.encode('utf-8')
    encoded_password = base64.b64encode(password_bytes)
    return encoded_password.decode('utf-8')

# Decode a password
def decode_password(encoded_password):
    encoded_password_bytes = encoded_password.encode('utf-8')
    password_bytes = base64.b64decode(encoded_password_bytes)
    return password_bytes.decode('utf-8')

# Store the password
def store_password(site, password):
    encoded_password = encode_password(password)
    with open("passwords.txt", "a") as file:
        file.write(f"{site}:{encoded_password}\n")

# Retrieve the password
def retrieve_password(site):
    if not os.path.exists("passwords.txt"):
        return None
    
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_site, encoded_password = line.strip().split(":")
            if stored_site == site:
                return decode_password(encoded_password)
    return None

def main():
    while True:
        choice = input("Do you want to (s)tore or (r)etrieve a password? (q to quit): ")
        if choice == "s":
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            store_password(site, password)
            print("Password stored successfully!")
        elif choice == "r":
            site = input("Enter the site name: ")
            password = retrieve_password(site)
            if password:
                print(f"The password for {site} is {password}")
            else:
                print(f"No password found for {site}")
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please select either 's', 'r', or 'q'.")

if __name__ == "__main__":
    main()
