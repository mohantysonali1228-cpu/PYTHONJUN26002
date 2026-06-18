# Create a Building Class

# Create a class
class Building:
    # Constructor with user input
    def __init__(self):
        self.building_name = input("Enter Building Name: ")
        self.location = input("Enter Location: ")
        self.number_of_floors = int(input("Enter Number of Floors: "))

    # Method to display building information
    def displayBuilding(self):
        print("\nBuilding Information")
        print("Building Name:", self.building_name)
        print("Location:", self.location)
        print("Number of Floors:", self.number_of_floors)

# Create an object
b1 = Building()

# Display building information
b1.displayBuilding()