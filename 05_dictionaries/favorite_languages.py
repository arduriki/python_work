favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print("")

# loop through key-value:
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("")

# loop through keys:
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# find out if a particular person was polled:
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print("")

# loop through keys in a particular order:
for name in sorted(favorite_languages.keys()):
    #sorted() -> alphabetical order
    print(f"{name.title()}, thank you for taking the poll.")
print("")

# loop through all values in a dictionary
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    # set() avoids value repetition
    print(language.title())
print("")

# Exercice 6-6
people = ['jordi', 'jen', 'efrain', 'phil', 'gloria']

for name in people:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for responding the poll!")
    elif name not in favorite_languages.keys():
        print(f"Please {name.title()}, respond the poll...")
print()

# * Lists inside a dictionary
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

# name => key, languages => values
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")