from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():  # If the file or folder exists, returns True.
        contents = path.read_text()
        username = json.loads(contents)  # Load the content
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)  # "Write the following in the file."
    return username


def greet_user():
    """Greet the user by name."""
    path = Path(
        '/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
