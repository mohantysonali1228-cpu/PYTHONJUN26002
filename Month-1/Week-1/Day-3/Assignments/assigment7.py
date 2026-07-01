# Create a simple ATM menu using Conditional Statements.
print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))
balance = 5000

if choice == 1:
    print("Your Balance is ₹", balance)

elif choice == 2:
    amount = int(input("Enter deposit amount: ₹"))
    balance += amount
    print("Updated Balance: ₹", balance)

elif choice == 3:
    amount = int(input("Enter withdrawal amount: ₹"))
    if amount <= balance:
        balance -= amount
        print("Updated Balance: ₹", balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Thank you for using the ATM.")

else:
    print("Invalid Choice")