def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('harry', 'hamster')  # Respecting order and overriding default value
describe_pet(animal_type='dog', pet_name='willie')  # Keyword argument
describe_pet('perseo')  # Respecting default values

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')