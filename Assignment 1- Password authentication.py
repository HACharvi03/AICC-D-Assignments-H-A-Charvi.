import hashlib
import os
import re
import getpass

def is_strong_password(password):
   
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, "Strong Password."

def hash_password(password, salt=None):
    """
    Hashes password with salt using SHA-256
    """
    if salt is None:
        salt = os.urandom(16)  # Generate random 16-byte salt

    password_bytes = password.encode('utf-8')
    hashed = hashlib.sha256(salt + password_bytes).hexdigest()

    return salt, hashed

users_db = {}

def register():
    print("\n===== USER REGISTRATION =====")
    username = input("Enter username: ")

    if username in users_db:
        print("Username already exists!")
        return

    password = getpass.getpass("Enter password: ")

    valid, message = is_strong_password(password)
    if not valid:
        print("Wrong", message)
        return

    salt, hashed_password = hash_password(password)
    users_db[username] = (salt, hashed_password)

    print(" Registration successful!")

def login():
    print("\n===== USER LOGIN =====")
    username = input("Enter username: ")

    if username not in users_db:
        print("❌ User does not exist!")
        return

    salt, stored_hash = users_db[username]

    attempts = 3
    while attempts > 0:
        password = getpass.getpass("Enter password: ")
        _, hashed_password = hash_password(password, salt)

        if hashed_password == stored_hash:
            print("Login successful!")
            return
        else:
            attempts -= 1
            print(f"Incorrect password! Attempts left: {attempts}")

    print("Account locked due to multiple failed attempts.")

def main():
    while True:
        print("\n==== PASSWORD AUTH SYSTEM ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
