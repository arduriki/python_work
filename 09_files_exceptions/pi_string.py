from pathlib import Path
"""Attempt to build a single string containing all the digits in the file with no whitespace in it."""

path = Path(
    '/home/arduriki/Dropbox/Python/python_work/09_files_exceptions/text_files/pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()


# print(f"{pi_string[:52]}...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
