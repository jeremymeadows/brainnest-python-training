# Create a BankAccount class with the following attributes: `balance` and
# `account_number`. The class should also have the following methods:
# `deposit(amount)`, `withdraw(amount)`, and `info()`.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def info(self):
        print(f'{self.account_number}: €{self.balance:0.2f}')


account = BankAccount('1234', 1_000)
account.info()
account.withdraw(127.90)
account.info()
account.deposit(511.63)
account.info()
