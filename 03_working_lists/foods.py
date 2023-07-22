my_foods = ['pizza', 'falafel', 'carrot cake', 'bagel']

# this copy doesn't work:
# friend_foods = my_foods

# this copy works, using slice:
friend_foods = my_foods[:] # copy full list

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)

# Slices exercise:
print("\nThe first three items in the list are:")
for my_food in my_foods[:3]:
    print(my_food)
#print(my_foods[:3])

print("\nThree items from the middle of the list are:")
for my_food in my_foods[1:4]:
    print(my_food)
#print(my_foods[1:4])

print("\nThe last three items in the list are:")
for my_food in my_foods[-3:]:
    print(my_food)
#print(my_foods[-3:])