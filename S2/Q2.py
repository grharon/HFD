from collections import namedtuple


class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

        return f"{self.name} with current balance {self.balance - amount}, deposit amount: {amount}"

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            return f"Your balance account is not sufficent. The amount to withdraw is {amount} and the current balance is {self.balance}"

        return f"{self.name} with current balance {self.balance + amount}, withdraw amount: {amount}"

    def __str__(self):
        return f"{self.name}'s account. Latest Balance: {self.balance}"


class DevAccount(Account):
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def setBalance(self, amount):
        self.balance = amount
        return self.balance

    def getBalance(self):
        return self.balance

    def transfer(self, amount, account):
        self.balance = self.balance - amount
        account.balance = account.balance + amount
        return f"{self.name} with current balance {self.balance + amount}, transfer to {account.name} amount: {amount} "


# Section 2 - Q1
# Customer 1
c1 = Account("A0000", "Ali", 0)
print("---Ali--")
print(c1.deposit(100))
print(c1)

# Customer 2
c2 = DevAccount("B0000", "Jim", 100)
print("---Jim--")
print(c2)
print(c2.transfer(50, c1))
print(c2)
print(c1)
