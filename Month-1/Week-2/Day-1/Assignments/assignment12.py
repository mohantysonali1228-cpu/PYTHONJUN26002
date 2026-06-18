# Create a Product Class
class Product:
    def __init__(self, product_name, category, price):
        self.product_name = product_name
        self.category = category
        self.price = price

    def display(self):
        print("Product Name:", self.product_name)
        print("Category:", self.category)
        print("Price:", self.price)
        print()


# Creating 3 product objects
p1 = Product("Laptop", "Electronics", 50000)
p2 = Product("Shampoo", "Personal Care", 250)
p3 = Product("Notebook", "Stationery", 100)

# Displaying product details
p1.display()
p2.display()
p3.display()