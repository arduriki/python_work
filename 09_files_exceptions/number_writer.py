from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)