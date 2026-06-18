
# Create a Constructor
# Create a class
class Employee:
    # Constructor
    def __init__(self, employee_name, employee_id, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.salary = salary

    # Method to display details
    def display(self):
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print()

# Create 3 employee objects
emp1 = Employee("John", 101, 50000)
emp2 = Employee("Alice", 102, 60000)
emp3 = Employee("David", 103, 55000)

# Display all employee details
emp1.display()
emp2.display()
emp3.display()