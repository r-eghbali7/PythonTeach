class Cat:
    def speak(self):
        print("Meow!")

class Dog:
    def speak(self):
        print("Woof!")

def animal_sound(animal):
    animal.speak()


c = Cat()
d = Dog()

animal_sound(c)  # Meow!
animal_sound(d)  # Woof!

# -----------------------------------------------

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * (5 ** 2)

class Square(Shape):
    def area(self):
        return 4 * 4


shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.area())
