# وقتی یه ویژگی رو با @property تعریف می‌کنی، روی دسترسی به اون کنترل کامل داری.

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance can't be negative!")
        self._balance = amount

acc = BankAccount(1000)
print(acc.balance)   
acc.balance = 500   
acc.balance = -200   

# ----------------------| CLASSIC MODEL |------------------------------------------

class Student:
    def __init__(self, grade):
        self.set_grade(grade)

    def set_grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            raise ValueError("Grade must be between 0 and 100")

    def get_grade(self):
        return self._grade


s = Student(85)
print(s.get_grade())  # ✅

# این مثال رو با استفاده از @property  بنویسد







# ----------------------------------------------------------------

class Product:
    def __init__(self, price):
        self.price = price  # در اصل داره setter رو صدا می‌زنه

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

# ----------------------------------------------------------------

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


t = Temperature(25)
print(t.fahrenheit)  # 77.0

t.celsius = 0
print(t.fahrenheit)  # 32.0
