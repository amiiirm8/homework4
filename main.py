from users import User
from typing import Tuple, Union
from typing import Optional

def register_user() -> None:
    """
    Registers a new user by taking input from the user and creating a User object.
    """
    username: str = input("Enter your username: ")
    password: str = input("Enter your password: ")
    phone_number: Optional[str] = input("Enter your phone number (optional): ")
    user: Optional[User] = User.create_user(username, password, phone_number)
    if user:
        print("User created successfully.")
    else:
        print("User creation failed.")

def login_user() -> None:
    """
    Logs in a user by taking input from the user and verifying the credentials.
    """
    username: str = input("Enter your username: ")
    password: str = input("Enter your password: ")
    user: Optional[User] = User.users.get(username)
    if user and user.password == password:
        print("Login successful.")
        while True:
            choice: str = input("Enter 1 to view user information, 2 to edit personal information, 3 to change password, or 4 to log out: ")
            if choice == "1":
                print(str(user))
            elif choice == "2":
                new_username: str = input("Enter new username (press enter to skip): ")
                new_phone_number: Optional[str] = input("Enter new phone number (press enter to skip): ")
                if new_username:
                    if User.is_username_taken(new_username):
                        print("This username is already taken. Please choose another one.")
                        continue
                    user.username = new_username
                if new_phone_number:
                    user.phone_number = new_phone_number
            elif choice == "3":
                old_password_1: str = input("Enter your old password: ")
                if old_password_1 == user.password:
                    new_password: str = input("Enter your new password: ")
                    new_password_repeat: str = input("Enter your new password again: ")
                    if new_password == new_password_repeat and User.is_valid_password(new_password):
                        user.password = new_password
                        print("Password changed successfully.")
                    else:
                        print("Invalid password. Password not changed.")
                else:
                    print("Incorrect password. Password not changed.")
            elif choice == "4":
                print("Logging out.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Incorrect username or password.")

def run_program() -> None:
    """
    Runs the program by displaying the user menu and taking input from the user.
    """
    while True:
        choice: str = input("Enter 0 to exit or 1 to register a new user, or 2 to log in: ")
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_program()