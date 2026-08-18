class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):

        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print("Retiro realizado")
        else:
            print("No se puede realizar el retiro")