from pathlib import Path

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    path = Path(
        f"/home/arduriki/Documents/Python/python_work/09_files_exceptions/text_files/{filename}")
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        # Print the names of the animals:
        names = contents.split()
        for name in names:
            print(name)
