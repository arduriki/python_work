from pathlib import Path

files = ['alice.txt', 'little_women.txt', 'moby_dick.txt']
word = input("Write a word to look up in the files: ")
word = word + " "
for file in files:
    path = Path(f"/home/arduriki/Documents/Python/python_work/09_files_exceptions/text_files/{file}")
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        num_words = contents.lower().count(word)
        print(f"The word {word} appears {num_words} times.")