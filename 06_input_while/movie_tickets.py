prompt = "How old are you?"
prompt += "\n(Enter 0 to exit) "

age = ""
active = age != 0

while active:
    age = input(prompt)
    age = int(age)

    if age == 0:
        break
    elif age < 3:
        print("You're free of charge.")
    elif 3 <= age <= 12:
        print("Your ticket's price is 10$.")
    else:
        print("Your ticket's price is 15$.")
