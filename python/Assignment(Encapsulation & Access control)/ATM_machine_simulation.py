class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Authentication Successful")
        else:
            print("Wrong PIN")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if not self.__authenticated:
            print("Please authenticate first")
            return

        self.__balance += amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if not self.__authenticated:
            print("Please authenticate first")
            return

        if amount > 20000:
            print("Withdrawal limit is ₹20,000")
            return

        if amount > self.__balance:
            print("Insufficient Balance")
            return

        self.__balance -= amount
        print("Withdrawal Successful")

    def mini_statement(self):
        if not self.__authenticated:
            print("Please authenticate first")
            return

        print("Owner:", self._owner)
        print("Current Balance:", self.__balance)


# Testing
a1 = ATM(1234, 50000, "Tanuj")

a1.authenticate(1234)

a1.deposit(5000)

a1.withdraw(10000)

a1.mini_statement()

print("Balance:", a1.balance)