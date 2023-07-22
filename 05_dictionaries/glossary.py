glossary = {
    'if-else': "If the condition is true, runs the code inside the if. Otherwise runs the else part.",
    'loop': "Repeat a sequence until reaches an end.",
    'list': "List of items stored in a variable.",
    'variable': "Like a container that stores a value.",
    'string': "Letters and numbers under quotation marks."
}

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
print("")

glossary['dictionary'] = 'It is a set of key-value items.'

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")