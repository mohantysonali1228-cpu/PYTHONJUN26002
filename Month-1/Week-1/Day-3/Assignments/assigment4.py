# Function declaration
def calculate_grade(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Grade F")

# Taking input
marks = int(input("Enter your marks: "))

# Function call
calculate_grade(marks)