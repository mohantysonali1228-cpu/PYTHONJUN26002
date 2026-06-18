
# Create a Book Class

# Create a class
class Book:
    # Constructor
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def displayBook(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

# Create an object
book1 = Book("Python Programming", "sonali", 500)

# Call the method
book1.displayBook()