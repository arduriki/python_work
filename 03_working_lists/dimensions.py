# Tuple: a list of items that cannot change.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# one value tuple: my_t = (3,)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
# reassigning the tuple variable
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)