def make_shirt(size="large", message="I love Python"):
    print(f"\nThe size of the t-shirt is: {size}.")
    print(f"It's message is: {message}")


make_shirt("L", "Están pasando cosas")
make_shirt(message="Están pasando cosas", size="L")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="Escudos!")