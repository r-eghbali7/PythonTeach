class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # ← private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())  # خروجی: 1200

acc.__balance = -99999  # ❌ این مقدار تغییر نمی‌کنه چون private هست
print(acc.get_balance())  # هنوز هم: 1200


# ---------------------------------------------------------------------------------

# Use @property
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
