def describe_city(name, country='spain'):
    print(f"\n{name.title()} is in {country.title()}")

describe_city('madrid')
describe_city(name='barcelona')
describe_city('reykjavik', 'iceland')