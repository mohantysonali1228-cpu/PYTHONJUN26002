# Create a Teacher Class

# Create a class
class Teacher:
    # Constructor
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    # Method to print teacher information
    def displayTeacher(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")

# Create an object
teacher1 = Teacher("sonali", "Python", 5)

# Call the method
teacher1.displayTeacher()