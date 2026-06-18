# Create a Car Class
# Create a class
class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

# Create 2 objects
car1 = Car("Toyota", "White", "Camry")
car2 = Car("Hyundai", "Black", "Creta")

# Print details of both cars
print("Car 1 Details")
print("Brand:", car1.brand)
print("Color:", car1.color)
print("Model:", car1.model)

print("\nCar 2 Details")
print("Brand:", car2.brand)
print("Color:", car2.color)
print("Model:", car2.model)