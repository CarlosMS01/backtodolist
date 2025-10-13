import re

def is_valid_email(email: str) -> bool:
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None

def is_valid_password(password: str) -> bool:
    return len(password) >= 8 and any(char.isdigit() for char in password)

def is_valid_username(username: str) -> bool:
    return len(username.strip()) >= 3