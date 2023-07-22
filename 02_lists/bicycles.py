bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # prints the list with all the details: brackets and apostrophes
print(bicycles[0].title()) # accessing the first position / index of the list
print(bicycles[1]) # second index position
print(bicycles[3]) # fourth index position
print(bicycles[-1]) # last item of the list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)