from pathlib import Path


path = Path(
    '/home/arduriki/Dropbox/Python/python_work/09_files_exceptions/text_files/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()  # creates a list with the lines

for line in lines:
    print(line)
