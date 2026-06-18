#  Create a Mobile Class

# Create a class
class Mobile:
    # Constructor
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    # Method to display mobile information
    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

# Create an object
mobile1 = Mobile("Samsung", "8GB", "128GB", 25000)

# Display mobile information
mobile1.display()