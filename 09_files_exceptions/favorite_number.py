from pathlib import Path
import json



path = Path('/Users/arduriki/Documents/Python/python_work/09_files_exceptions/json_files/fav_number.json')
if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I know your favorite number! It's {fav_number}")
else:
    fav_number = int(input("What is your favorite number? "))
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print("I'll remember your favorite number!")