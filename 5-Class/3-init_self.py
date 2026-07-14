class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


p1 = BankAccount()
p1.deposit(100)
p1.withdraw(10)
p1.show_balance()


# -----------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Sara")
p1.greet()          # Hello, my name is Sara
p1.change_name("Mina")
p1.greet()          # Hello, my name is Mina

