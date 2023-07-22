motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modify elements from a list
motorcycles[0] = 'ducati'
print(motorcycles) # Rest of the list remains the same

# append elements to the end of the list
motorcycles.append('honda')
print(motorcycles)

# usefull for an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert an element
motorcycles.insert(0, 'ducati')
print(motorcycles) # moves the previous 0 element to the right

# remove an element from the list
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop() method -> remove the last item of the list and work with it
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# remove() is useful to remove a value of a certain list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
