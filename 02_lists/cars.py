cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # alphabetical order permanently
print(cars)

cars.sort(reverse=True) # reverse alphabetical order
print(cars)

#############

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # temporarily sorted in alphabetical order

print("\nHere is the original list again:")
print(cars)

print("\nAnd now with reverse alphabetical order:")
print(sorted(cars, reverse=True))

#############

cars = ['bmw', 'audi', 'toyota', 'subaru'] # owned in chronological order
print(cars)

cars.reverse() # reverse chronological order or reverses the list
print(cars)

cars.reverse() # again for the original order
print(cars)

print(len(cars)) # len() shows the number of items the list contains
# Python starts counting with one