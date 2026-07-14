name = "Ali"
age = 30

def say_hello():
    print(f"Hello, {name}")

say_hello()

# -----------------------------------------------

class Person:
    def __init__(self, name, age): # متد سازنده
        self.name = name
        self.age = age

    def say_hello(self): # متد 
        print(f"Hello, {self.name}") 

p = Person("Ali", 30) # نمونه سازی
p.say_hello() # استفاه از نمونه سازی
