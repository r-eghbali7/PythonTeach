class Parent:
    # ویژگی‌ها و متدهای والد
    ...

class Child(Parent):
    # ویژگی‌ها و متدهای جدید یا بازنویسی شده
    ...

# -----------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):  # Dog فرزند Animal
    def bark(self):
        print(f"{self.name} barks!")

dog1 = Dog("Rex")
dog1.speak()  # Rex makes a sound.
dog1.bark()   # Rex barks!

# Override Methode Speak   *****************************************
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

cat1 = Cat("Kitty")
cat1.speak()  # Kitty says Meow!

# -----------------------------------------------

# Super With  __init__
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)     # فراخوانی سازنده‌ی والد
        self.student_id = student_id


# Super Whit Method
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # اجرای متد والد
        print("Dog barks")

# -----------------------------------------------
