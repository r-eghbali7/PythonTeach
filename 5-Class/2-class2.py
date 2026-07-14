class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")

my_car = Car("Toyota", "Red")
print(my_car.brand)  # خروجی: Toyota
print(my_car.color)  # خروجی: Red

# -----------------------------------------------

class Student:
    def __init__(self, name, grade):   # متد خاص برای مقداردهی ویژگی‌ها
        self.name = name               # ویژگی ۱
        self.grade = grade             # ویژگی ۲

    def introduce(self):               # متد معرفی
        print(f"My name is {self.name} and I am in grade {self.grade}.")


s1 = Student("Sara", 10)
s1.introduce()

# -----------------------------------------------

class Dog:
    def __init__(self, name, age):
        self.name = name      # ویژگی name
        self.age = age        # ویژگی age

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Max", 3)
dog1.bark()  # خروجی: Max says Woof!
