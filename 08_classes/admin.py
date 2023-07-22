from user import User


class Privileges:
    """Know the privileges of a user."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"\nThese are user's privileges:")
        for privilege in self.privileges:
            print(f"· {privilege}")


class Admin(User):
    """Attempt to create an Admin user class, inheriting from User"""

    def __init__(self, first_name, last_name, nickname, email):
        """Initialize attributes from the class"""
        super().__init__(first_name, last_name, nickname, email)
        self.privileges = Privileges()