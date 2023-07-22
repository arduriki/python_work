from pathlib import Path

prompt = input("What is your name? (type 'exit' to stop) > ").lower()
user = prompt.title() + "\n"

while prompt != 'exit':
    prompt = input("What is your name? (type 'exit' to stop) > ").lower()
    if prompt == 'exit':
        break
    else:
        user += prompt.title() + "\n"

path = Path('/Users/arduriki/Dropbox/Python/python_work/09_files_exceptions/guest_book.txt')
path.write_text(user)
