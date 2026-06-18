# Create a Citizen Class

# Create a class
class Citizen:
    # Class variable
    country = "India"

    # Constructor
    def __init__(self, aadhaar_number, phone_number, name):
        self.aadhaar_number = aadhaar_number
        self.phone_number = phone_number
        self.name = name

    # Method to print all details
    def display(self):
        print("Name:", self.name)
        print("Aadhaar Number:", self.aadhaar_number)
        print("Phone Number:", self.phone_number)
        print("Country:", Citizen.country)

# Create an object
citizen1 = Citizen("1234-5678-9012", "9876543210", "sonali")

# Print details
citizen1.display()