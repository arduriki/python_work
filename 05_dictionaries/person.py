people = {
    'gromeu': {
        'first_name': 'gloria',
        'last_name': 'romeu',
        'city': 'moia',
    },

    'egarcia': {
        'first_name': 'efrain',
        'last_name': 'garcia',
        'city': 'manlleu',
    },

    'iyagues': {
        'first_name': 'isaac',
        'last_name': 'yagues',
        'city': 'vic',
    },

}

for nickname, user_info in people.items():
    print(f"\nNickname: {nickname}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
