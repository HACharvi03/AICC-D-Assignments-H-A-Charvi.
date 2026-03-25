import getpass

# Create password
password = getpass.getpass("Create a strong password: ")

# Check password strength
if len(password) < 8:
    print("Password too weak! Must be at least 8 characters.")
else:
    print("Password created successfully!")

    # Login system with 3 attempts
    attempts = 3
    while attempts > 0:
        entered = getpass.getpass("Enter password: ")

        if entered == password:
            print("Access Granted ✅")
            break
        else:
            attempts -= 1
            print(f"Wrong password! Attempts left: {attempts}")

    if attempts == 0:
        print("Access Denied ❌")