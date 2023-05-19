import uuid
from typing import Optional, Dict



class User:
    """
    A class representing a user.

    Attributes:
    ----------
    username : str
        The username of the user.
    password : str
        The password of the user.
    phone_number : Optional[str]
        The phone number of the user (optional).
    id : str
        The unique identifier of the user.
    """
    users: Dict[str, 'User'] = {}

    def __init__(self, username: str, password: str, phone_number: Optional[str] = None) -> None:
        """
        Initializes a new instance of the User class.

        Parameters:
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.
        phone_number : Optional[str]
            The phone number of the user (optional).
        """
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.id = str(uuid.uuid4())

    @classmethod
    def create_user(cls, username: str, password: str, phone_number: Optional[str] = None) -> Optional['User']:
        """
        Creates a new user and adds it to the list of users.

        Parameters:
        ----------
        username : str
            The username of the user.
        password : str
            The password of the user.
        phone_number : Optional[str]
            The phone number of the user (optional).

        Returns:
        -------
        Optional[User]
            The newly created User object, or None if the creation fails.
        """
        if cls.is_username_taken(username):
            print("This username is already taken. Please choose another one.")
            return None
        
        if not cls.is_valid_password(password):
            print("Password must be at least 4 characters long.")
            return None
        
        user = cls(username, password, phone_number)
        cls.users[user.username] = user
        return user

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        Checks if a password is valid.

        Parameters:
        ----------
        password : str
            The password to check.

        Returns:
        -------
        bool
            True if the password is valid, False otherwise.
        """
        return len(password) >= 4
    

    @classmethod
    def is_username_taken(cls, username: str) -> bool:
        """
        Checks if a username is already taken.

        Parameters:
        ----------
        username : str
            The username to check.

        Returns:
        -------
        bool
            True if the username is already taken, False otherwise.
        """
        return username in cls.users.keys()

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
        -------
        str
            The string representation of the user.
        """
        return f"Username: {self.username}\nID: {self.id}\nPhone Number: {self.phone_number}"