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

# Section 2 - Q1


# Instance Customer 1
c1 = Account("A0000", "Ali", 0)
print("---Ali--")
print(c1.deposit(100))
print(c1)

# Instance Customer 2
c2 = Account("A0001", "Muthu", 1000)
print("---Muthu--")
print(c2.withdraw(1001))
print(c2)

# Instance Customer 3
c3 = Account("A0002", "Chong", 2000)
print("---Chong--")
print(c3.deposit(100))
print(c3)
print(c3.withdraw(100))
print(c3)

# b) store them in a data structure chosen : namedtuple
# Reason: Kinda like easy and immutable data structures, but not suitable for dynamic variable field such as balance

Customer = namedtuple('Customer', ['id', 'name', 'balance'])

Customers = [
    Customer(c1.id, c1.name, c1.balance),
    Customer(c2.id, c2.name, c2.balance),
    Customer(c3.id, c3.name, c3.balance),
]

print(Customers[0])
print(Customers[1])
print(Customers[2])
