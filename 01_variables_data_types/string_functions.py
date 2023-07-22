print("\tPython") # tab
print("Languages:\nPython\nC\nJavaScript") # new line
print("Languages:\n\tPython\n\tC\n\tJavaScript") # combined

favorite_language = 'python '
print(favorite_language.rstrip()) # no whitespace at the right side temporarily
favorite_language = favorite_language.rstrip() # ensure that whitespace is removed
print(favorite_language)

favorite_language = ' python'
print(favorite_language.lstrip()) # remove left whitespace

favorite_language = ' python '
print(favorite_language.strip()) # remove both sides whitespaces

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) # removes prefix indicated
simple_url = nostarch_url.removeprefix('https://') # remove it permanently and assigned to another variable
