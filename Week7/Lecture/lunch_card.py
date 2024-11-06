class LunchCard:
    def __init__(self, name, id, initial_balance):
        self.name = name
        self.id = id
        self.balance = initial_balance
    
    def depositMoney(self, amount):
        if isinstance(amount, int) or isinstance(amount, float):
            if amount > 0:
                self.balance += amount
            else:
                print("Amount should be a positive value!")
        else:
            print("Amount information should be numerical!")
    
    def displayCurrentBalance(self):
        print("The balance for " + self.name + " with ID " + str(self.id) + " is " + str(self.balance))

    def payLunch(self, lunchPrice):
        if isinstance(lunchPrice, int) or isinstance(lunchPrice, float):
            if lunchPrice <= self.balance:
                self.balance -= lunchPrice
                print("Payment is successful")
            else:
                print("You don't have enough balance to eat this lunch")
        else:
            print("Price information should be numerical!")

# main
peter = LunchCard("Peter", 1, 20)
alice = LunchCard("Alice", 2, 30)

peter.payLunch(10)
alice.payLunch(12)

peter.displayCurrentBalance()
alice.displayCurrentBalance()

peter.depositMoney(5)
peter.payLunch(16)

alice.payLunch(14)

peter.displayCurrentBalance()
alice.displayCurrentBalance()