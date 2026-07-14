class BankAccount:
    def __init__(self):
        self.balance = 5

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



class bank1(BankAccount):
    def deposit(self, amount):
        super().deposit(amount)
        print(self.balance)
    
a = bank1()
a.deposit(5)

# -----------------------------------------------

# Tamrin
class Employee:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"Employee name: {self.name}")

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def get_info(self):
        super().get_info()
        print(f"Department: {self.department}")
