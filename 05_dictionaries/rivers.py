rivers = {
    'amazon': 'brasil',
    'nile': 'egypt',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("")

for river in sorted(rivers.keys()):
    print(f"{river.title()} is a major river.")
print("")

for country in rivers.values():
    print(f"{country.title()} is a country where a major river runs through.")