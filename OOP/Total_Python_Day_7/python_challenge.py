class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):
    def __init__(self, first_name, last_name, account_number):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = 0

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw more than the current balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

def create_customer():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    account_number = input("Enter account number: ")
    return Customer(first_name, last_name, account_number)

def main():
    customer = create_customer()

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            customer.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            customer.withdraw(amount)
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
