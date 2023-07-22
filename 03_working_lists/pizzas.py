pizzas = ['margarita', 'hawaiana', 'barbacoa']

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.\n")

print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('cabramelizada')
friend_pizzas.append('carbonara')

print("My favorite pizzas are:")
print(pizzas)

print("My friend's favorite pizzas are:")
print(friend_pizzas)