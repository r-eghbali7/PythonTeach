from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * (5 ** 2)

class Square(Shape):
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]
for s in shapes:
    print(s.area())

















# tamrin
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

vehicles = [Car(), Motorcycle()]
for v in vehicles:
    v.start_engine()
