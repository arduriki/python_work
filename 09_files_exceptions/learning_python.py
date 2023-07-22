from pathlib import Path

"""Prints the contents of a text file once by reading in the entire file,
and once by storing the lines in a list and then looping over each line."""

path = Path('/Users/arduriki/Dropbox/Python/python_work/09_files_exceptions/learning_python.txt')
contents = path.read_text()
print(contents)
print()

# Replace the word Python with the name of another language.
contents = contents.replace('Python', 'Java')

for line in contents.splitlines():
    print(line)
