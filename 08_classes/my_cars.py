# Import some classes
# from car import Car, ElectricCar
# my_mustang = Car('ford', 'mustang', 2024)
# my_leaf = ElectricCar('nissan', 'leaf', 2024)

# import car as c

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

from car import Car
# from electric_car import ElectricCar as EC
import electric_car as ec


my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())