from pathlib import Path

user = input("What is your name? > ").lower()

path = Path('/Users/arduriki/Dropbox/Python/python_work/09_files_exceptions/guest.txt')
path.write_text(user.title())
