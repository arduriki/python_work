from car import ElectricCar


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

vw_id3 = ElectricCar('volkswagen', 'id3', 2023)
vw_id3.battery.get_range()
vw_id3.battery.upgrade_battery()
vw_id3.battery.get_range()
