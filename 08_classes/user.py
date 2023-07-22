class User:
    """Model a user"""

    def __init__(self, first_name, last_name, nickname, email):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"\nUser's full name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"His/Her nickname is {self.nickname}.")
        print(f"His/her email is {self.email}.")

    def greet_user(self):
        print(f"\nHello {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0