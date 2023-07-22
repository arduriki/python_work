prompt = "Which topping would you like in your pizza? "
prompt += "\n(Write 'quit' to stop) "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    print(f"Adding {topping}!")
