from pathlib import Path
import json

path = Path('/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")