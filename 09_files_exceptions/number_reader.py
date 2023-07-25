from pathlib import Path
import json

path = Path('/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/numbers.json')
contents = path.read_text()  # Reads the text
numbers = json.loads(contents)  # Loads the content into the variable

print(numbers)
