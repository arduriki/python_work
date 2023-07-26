def city_name(city, country, population=''):
    """Generates a city's name and its country."""
    if population:
        full_city = f"{city.title()}, {country.title()} population {population}"
    else:
        full_city = f"{city.title()}, {country.title()}"
    return full_city
