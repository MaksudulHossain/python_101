class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"name: {self.restaurant_name}, type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        for flvaor in self.flavors:
            print(flvaor)
flavors = ["vanilla", "mango", "strawberry"]
ice1 = IceCreamStand("igloo", "italian", flavors)
ice1.display_flavors() 