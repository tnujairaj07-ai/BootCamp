class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

a1 = BankAccount()
a2 = BankAccount()

a1.deposit(1000)
print("A1 Balance:", a1.balance)

a1.withdraw(300)
print("A1 Balance:", a1.balance)

a2.deposit(650)
print("A2 Balance:", a2.balance)

a2.withdraw (600)
print("A2 Balance:", a2.balance)

a2.withdraw(700)
print("A2 Balance:", a2.balance)

