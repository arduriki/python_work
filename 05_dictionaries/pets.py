pets = {
    'cat':{
        'name': 'perseo',
        'age': 1,
        'owner': 'claudia ferrer',
    },

    'dog':{
        'name': 'hugo',
        'age': 2,
        'owner': 'antonia gonzalez',
    },

    'bird':{
        'name': 'piu piu',
        'age': 4,
        'owner': 'jose ardura',
    },

}

for pet, pet_info in pets.items():
    print(f"\nThe following pet is a: {pet}")
    print(f"\tIts name is {pet_info['name'].title()}.")
    if pet_info['age'] == 1:
        print(f"\tIts age is {pet_info['age']} year old.")
    else:
        print(f"\tIts age is {pet_info['age']} years old.")
    print(f"\tIts owner is {pet_info['owner'].title()}.")