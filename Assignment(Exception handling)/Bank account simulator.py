class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=1000):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid deposit amount")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount


acc = BankAccount()

for action, amount in [("deposit", 500),
                       ("withdraw", 200),
                       ("deposit", -50),
                       ("withdraw", 2000)]:
    try:
        if action == "deposit":
            acc.deposit(amount)
        else:
            acc.withdraw(amount)

        print(f"{action} ₹{amount} successful. Balance = ₹{acc.balance}")

    except (InvalidAmountError, InsufficientFundsError) as e:
        print("Error:", e)

print("Final Balance =", acc.balance)