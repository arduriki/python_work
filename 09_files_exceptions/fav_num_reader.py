from pathlib import Path
import json

path = Path('/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/fav_number.json')
contents = path.read_text()
fav_number = json.loads(contents)

print(f"I know your favorite number! It's {fav_number}.")