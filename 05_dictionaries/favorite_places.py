favorite_places = {
    'pablo': ['paris', 'london', 'new york'],
    'maria': ['madrid', 'valencia'],
    'juan': ['tokyo', 'osaka', 'kyoto', 'barcelona'],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for city in places:
        print(f"\t{city.title()}.")