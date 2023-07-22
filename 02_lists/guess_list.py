people = ['chakib', 'efrain', 'marc']

message_chakib = f"Would you like to eat hamburger again {people[0].title()}?"
print(message_chakib)

message_efrain = f"There's a place that I would like you to try {people[1].title()}."
print(message_efrain)

message_marc = f"{people[2].title()}, would you like to come to dinner with me?"
print(message_marc)

################################

print(f"{people[1].title()} can't make it... ")

people[1] = 'andrea'
message_andrea = f"{people[1].title()} would love to eat hamburger in BCN!"
print(message_andrea)

#################################

print("Hey! I've found a bigger table!")

people.insert(0, 'dario')
people.insert(2, 'isaac')
people.append('juanan')

message_dario = f"Hey {people[0].title()}! I'd like to invite you for dinner! Would you like to come?"
print(message_dario)
message_isaac = f"I would like you to come to a fantastic place for dinner, {people[2].title()}!"
print(message_isaac)
message_juanan = f"There's a place in BCN to eat that you'd love, {people[-1].title()}!"
print(message_juanan)

##################################

print("I'm really sorry... But I can only invite two people for dinner!")

isaac = people.pop(2)
print(f"I'm sorry {isaac.title()}, but I can't count on you...")

marc = people.pop(3)
print(f"I'm sorry {marc.title()}, but I can't count on you...")

juanan = people.pop()
print(f"I'm sorry {juanan.title()}, but I can't count on you...")

chakib = people.pop(1)
print(f"I'm sorry {chakib.title()}, but I can't count on you...")

message_dario = f"Hey {people[0].title()}! You're still in for dinner! YAY!"
print(message_dario)

message_andrea = f"Hey {people[-1].title()}! You're still in for dinner! YAY!"
print(message_andrea)

##############

print(f"\nThe number of people that I can invite is: {len(people)}")