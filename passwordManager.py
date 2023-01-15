from cryptography.fernet import Fernet
#  pip install cryptography

# Encryption. Comment out this function after using it ONCE! The Key.key file will generate.
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Temporary password
master_password = "admin"

# Functions
def add_new_password():
    print("You have selected 'Add a new password'")
    # Get Account name
    new_account = input("Enter the 'Account Name: ")
    # Get username
    new_username = input("Enter the 'Username': ")
    # Get password
    new_password = input("Enter the 'Password': ")

    confirm_password = ""  # Set empty password confirmation
    while new_password != confirm_password:  # Confirm the password
        confirm_password = input("Please Confirm the 'Password': ")

    # Open/Create file called "passwords.txt" in 'append' mode.
    with open("passwords.txt", "a") as password_file:
        # Add the new account/username/password
        password_file.write(f"{new_account},{new_username},{fer.encrypt(confirm_password.encode()).decode()}\n")


def view_all_passwords():
    with open("passwords.txt", "r") as password_file:
        print("=============================================")
        for entry in password_file.readlines():
            # Account: 0, Username: 1, Password: 2
            detail = entry.rstrip()
            account, username, password = detail.split(",")
            print(f"Account: {account}")
            print(f"Username: {username}")
            print(f"Password: {fer.decrypt(password.encode()).decode()}")
            print("=============================================")


# Ask for password
pwd = input("Enter Password: ")
while True:  # Keep asking until correct password is input
    if pwd == master_password:
        break
    else:
        print("Incorrect password. Please try again.")
        pwd = input("Enter Password: ")

# LOGGED IN!
print("Welcome Back!")
key = load_key()
fer = Fernet(key)

# Find out if the user wants to Add/View passwords or Exit the program.
while True:
    mode_input = input("""Do you want to view passwords or add a new one?
Type 'Add', 'View' or 'Quit'
""").lower()
    if mode_input == "add":  # ADD NEW PASSWORD
        add_new_password()
    elif mode_input == "view":  # VIEW PASSWORDS
        view_all_passwords()
    elif mode_input == "quit":  # QUIT PROGRAM
        break
    else:
        print("Invalid input. Please try again! ")  # KEEP ASKING!