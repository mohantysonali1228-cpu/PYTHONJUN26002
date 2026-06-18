
# Create a Bank Account Class
# Create a class
class BankAccount:
    # Constructor
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    # Method to display account details
    def displayAccount(self):
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

# Create an object
account1 = BankAccount("sonali", 123456789, 50000)

# Display account details
account1.displayAccount()