players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# automatically starts with the 1st element
print(players[:4])
# starting from a certain item til the end
print(players[2:])
# if you want to print the last items:
print(players[-3:])
# third value to indicate how many items to skip
print(players[0:4:2])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

