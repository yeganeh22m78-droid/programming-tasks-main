# File: auth_lib.py
# Library for handling user login and registration
# Written in a simple style, like a student project

import hashlib
import os

# Constant for the credentials file
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hashPassword(password: str) -> str:
    """
    Hash the password using MD5.
    Returns the hex string of the hash.
    """
    return hashlib.md5(password.encode()).hexdigest()


def registerUser(username: str, password: str) -> None:
    """
    Register a new user by writing their username and hashed password
    into the credentials file.
    """
    hashed = hashPassword(password)

    # Figure out the next ID number
    next_id = 0
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                if last_line:
                    next_id = int(last_line.split(DELIMITER)[0]) + 1

    # Append the new user to the file
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{next_id}{DELIMITER}{username}{DELIMITER}{hashed}\n")


def loginUser(username: str, password: str) -> bool:
    """
    Check if the given username and password match
    something in the credentials file.
    """
    hashed = hashPassword(password)

    if not os.path.exists(CREDENTIALS_FILE):
        return False

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3:
                _, stored_username, stored_hash = parts
                if stored_username == username and stored_hash == hashed:
                    return True
    return False
