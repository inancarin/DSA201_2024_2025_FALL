from bank_account import BankAccount

account1 = BankAccount(1, "Alice")
account2 = BankAccount(2, "Bob")
account1.deposit(100)
account1.withdraw(50)
account1.display_balance()
account2.display_balance()
