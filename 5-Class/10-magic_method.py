class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages


b = Book("Python Basics", 300)

print(b)         # Book: Python Basics
print(len(b))    # 300

# --------------------------------------------------

# add

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        new_title = self.title + " & " + other.title
        new_pages = self.pages + other.pages
        return Book(new_title, new_pages)


b1 = Book("OOP", 200)
b2 = Book("Data Structures", 250)

b3 = b1 + b2
print(b3)          # OOP & Data Structures (450 pages)
print(len(b3))     # 450


# repr
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name='{self.name}')"

p = Person("Reza")
print(repr(p))  # خروجی: Person(name='Reza')


# eq:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # خروجی: True


# __lt__, __gt__
class Score:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

s1 = Score(70)
s2 = Score(90)
print(s1 < s2)  # خروجی: True


#__getitem__ 
class ShoppingList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

shop = ShoppingList(["milk", "bread", "eggs"])
print(shop[1])  # خروجی: bread


# __setitem__ 
class ShoppingList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

shop = ShoppingList(["milk", "bread", "eggs"])
shop[1] = "cheese"
print(shop.items)  # خروجی: ['milk', 'cheese', 'eggs']


# __contains__ 
class Basket:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

b = Basket(["apple", "banana"])
print("apple" in b)  # خروجی: True


# __call__ 
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}!")

g = Greeter("Nima")
g()  # خروجی: Hello, Nima!


# __del__ 
class Demo:
    def __del__(self):
        print("Object destroyed!")

d = Demo()
del d  # خروجی: Object destroyed!

