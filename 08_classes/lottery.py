import random

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')
my_ticket = random.sample(my_tuple, 6)


# Write a loop that keeps pulling numbers until my_ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.

winning_ticket = random.sample(my_tuple, 6)


attempts = 0
while my_ticket != winning_ticket:
    winning_ticket = random.sample(my_tuple, 6)
    attempts += 1
    print(f"Attempt #{attempts}: {winning_ticket}")

print(f"\nMy ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"\nYou won after {attempts} attempts!")
