class BankAccount:
    def __init__(self, ID, account_holder):
        self.ID = ID
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def display_balance(self):
        print("Current balance:", self.balance)