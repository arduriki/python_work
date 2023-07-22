def city_country(name, country):
    cc_full = f"{name}, {country}"
    return cc_full.title()

city1 = city_country("barcelona", "spain")
print(city1)

city2 = city_country("london", "england")
print(city2)

city3 = city_country("paris", "france")
print(city3)
