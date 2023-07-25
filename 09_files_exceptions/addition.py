while True:
    try:
        number1 = int(input("Write a number: "))
        number2 = int(input("Write another number: "))
    except ValueError:
        print("Sorry, you have to write a number.")
    except KeyboardInterrupt:
        print("Program closed.")
        break
    else:
        number1 = str(number1)
        number2 = str(number2)
        two_digit = number1 + number2
        print(f"Here's your two-digit number: {two_digit}")