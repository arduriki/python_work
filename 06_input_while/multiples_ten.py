number = input("Tell me a number and I'd say if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of ten.")
else:
    print(f"\nThe number {number} is not multiple of ten.")
