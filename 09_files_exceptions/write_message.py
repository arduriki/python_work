from pathlib import Path


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('/Users/arduriki/Dropbox/Python/python_work/09_files_exceptions/programming.txt')
path.write_text(contents)
