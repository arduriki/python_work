from pathlib import Path
import json


def get_stored_user(path):
    """Get stored user's data if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_user(path):
    """Prompt for a new user's data."""
    user = {}
    user['name'] = input("What is your name? ").lower()
    user['last'] = input("What is your last name? ").lower()
    user['age'] = input("How old are you? ")
    contents = json.dumps(user)
    path.write_text(contents)
    return user


def greet_user():
    """Greet the user by name."""
    path = Path(
        '/home/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/user.json')
    user = get_stored_user(path)
    current_user = input("What's your user's name? ")
    if user['name'] == current_user:
        print("Welcome back! Here's your data:")
        for k, v in user.items():
            print(f"Your {k} is {v.title()}.")
    else:
        print("Let's create a new user for you then.")
        user = get_new_user(path)  # Overwrites the json file.
        print("Now I know some of your data.")


greet_user()
