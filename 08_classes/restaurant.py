class Restaurant:
    """Model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"\nThe restaurant's name is {self.restaurant_name}")
        print(f"Its cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Indicates that the restaurant is open."""
        print("The restaurant is open.")

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("You can't roll back the number of customers served!")

        return self.number_served

    def increment_number_served(self, customers_served):
        if customers_served > 0:
            self.number_served += customers_served
        else:
            print("You can't roll back the number of customers served!")

        return self.number_served






