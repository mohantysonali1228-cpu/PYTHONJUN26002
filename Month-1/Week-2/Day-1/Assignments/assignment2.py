# Create a Student Class
# Create a class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display student details
    def displayStudent(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create an object
student1 = Student("sonali", 22, "Python")

# Call the method
student1.displayStudent()