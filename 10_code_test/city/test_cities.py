from city_functions import city_name


def test_city_country():
    """Test if Santiago, Chile is well returned."""
    full_city = city_name('santiago', 'chile')
    assert full_city == 'Santiago, Chile'


def test_city_country_population():
    """Test if Santiago, Chile 5000000 is well returned."""
    full_city = city_name('santiago', 'chile', 5_000_000)
    assert full_city == 'Santiago, Chile population 5000000'
