# Create a Laptop Class

# Create a class
class Laptop:
    # Constructor
    def __init__(self, brand, processor, ram, price):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.price = price

    # Method to display laptop details
    def display(self):
        print("Brand:", self.brand)
        print("Processor:", self.processor)
        print("RAM:", self.ram)
        print("Price:", self.price)
        print()

# Create 3 laptop objects
laptop1 = Laptop("Dell", "Intel i5", "8GB", 50000)
laptop2 = Laptop("HP", "Intel i7", "16GB", 70000)
laptop3 = Laptop("Lenovo", "AMD Ryzen 5", "8GB", 55000)

# Display all laptop details
laptop1.display()
laptop2.display()
laptop3.display()