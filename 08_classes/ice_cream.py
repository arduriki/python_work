from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'cookie cream', 'mint']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)