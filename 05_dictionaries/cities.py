cities = {
    'barcelona': {
        'country': 'spain',
        'population': 5_575_000,
        'fact': 'Barcelona is the capital of Catalonia.',
    },

    'madrid': {
        'country': 'spain',
        'population': 6_642_000,
        'fact': 'Madrid is the capital of Spain.',
    },

    'tokyo': {
        'country': 'japan',
        'population': 13_929_000,
        'fact': 'Tokyo is the capital of Japan.',
    },
}

for city, city_data in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tThe city belongs to {city_data['country'].title()}.")
    print(f"\tIts population is: {str(city_data['population'])}.")
    print(f"\tIts fact is: {city_data['fact']}")
