favorite_numbers = {
    'raquel': [3, 4],
    'abel': [6, 34, 28],
    'efrain': [17],
    'ruben': [5, 65, 31, 98],
    'gabriel': [10, 9, 54, 82, 76],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}' favorite number is:")
    for number in numbers:
        print("\t"+str(number))