languages = ['spanish', 'catalan', 'english', 'french', 'italian']

# using individual values from a list
print(f"At home I usually speak {languages[0].title()}.")

# modify an element
languages[1] = 'portuguese'
print(languages)

# appending elements at the end
languages.append('catalan')
print(languages)

# inserting elements in the list, moves the existing element to the right
languages.insert(3, 'norwegian')
print(languages)

# popping the last item, storing the value in a variable
popped_language = languages.pop()
print(languages)
print(popped_language)

# popping a desired value into a variable
another_language = languages.pop(1)
print(languages)
print(another_language)

# remove an item by value
not_used_language = 'italian'
languages.remove(not_used_language)
print(languages)

# sort in alphabetical order
print(sorted(languages))
print(languages)

# reverse-alphabetical order
print(sorted(languages, reverse=True))
print(languages)

# reverse chronological order
languages.reverse()
print(languages)

# back to chronological order
languages.reverse()
print(languages)

# alphabetical order permanently
languages.sort()
print(languages)

# reverse-alphabetical order permanently
languages.sort(reverse=True)
print(languages)
