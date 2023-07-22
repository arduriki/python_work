from restaurant import Restaurant
from ice_cream import IceCreamStand

restaurant = Restaurant('Celler d\'en Miquel', 'catalan')

print(restaurant.restaurant_name+", "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 10
print(f"The restaurant has served {restaurant.number_served} customers.")

num_customers = restaurant.set_number_served(15)
print(f"\nThe restaurant has served {num_customers} customers.")

customers_served = restaurant.increment_number_served(20)
print(f"\nThe restaurant has served {customers_served} customers.")

la_real = Restaurant('La Real', 'american')
piccolo_biondo = Restaurant('Piccolo Biondo', 'pizzeria')
trinacria = Restaurant('Trinacria', 'italian')

la_real.describe_restaurant()
piccolo_biondo.describe_restaurant()
trinacria.describe_restaurant()

ice_cream = IceCreamStand('Xixo Vic', 'ice cream')
ice_cream.describe_restaurant()
ice_cream.display_flavors()
