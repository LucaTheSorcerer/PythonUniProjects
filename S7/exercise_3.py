class Auto:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

class Statistics:
    def __init__(self):
        self.autos = []

    def add_auto(self, auto):
        self.autos.append(auto)

    def anzahl_auto_farbe(self, color):
        anzahl = 0
        for auto in self.autos:
            if auto.color == color:
                anzahl += 1

        return  anzahl

    def avg_baujahr(self, brand):
        sum = 0
        year = 0
        nr = 0
        for auto in self.autos:
            if auto.brand == brand:
                year += auto.year
                nr += 1
        return year / nr

def main():
    ford1 = Auto("Ford", "Mustang", 2010, "blue")
    ford2 = Auto("Ford", "Mustang1", 2005, "green")
    mercedes = Auto("Mercedes", "G-Class", 2011, "green")
    stats = Statistics()
    stats.add_auto(ford1)
    stats.add_auto(ford2)

    print(stats.anzahl_auto_farbe('blue'))
    print(stats.avg_baujahr(2010))
main()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Circle:

    def __init__(self, r, c):
        self.r = r #Number
        self.c = c #point

    def print(self):
        print(f'radius: {self.r}, center: {(self.c.x, self.c.y)}')

    def move(self, dx, dy):
        self.c = Point(self.c.x + dx, self.c.y + dy)

        # self.c.x += dx
        # self.c.y += dy

    def resize(self, k):
        self.r *= k

    def area(self):
        from math import pi
        return pi*self.r**2


class Circle2:

    def __init__(self, r, x, y):
        self.r = r  # Number
        self.c = Point(x, y)  # point

    def print(self):
        print(f'radius: {self.r}, center: {(self.c.x, self.c.y)}')

    def move(self, dx, dy):
        self.c = Point(self.c.x + dx, self.c.y + dy)

        # self.c.x += dx
        # self.c.y += dy

    def resize(self, k):
        self.r *= k

    def area(self):
        from math import pi
        return pi * self.r ** 2

class Student:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age


def main():
    bob = Student("bob", 20)
    dob = Student("dob")

    print(bob.age, bob.name)
    print(dob.age, dob.name)
    c = Circle(10, Point(1,2))
    p = Point(1, 2)
    c1 = Circle(10, p)
    c.print()

    c2 = Circle2(10, 1, 2)

    c.move(10, 20)
    c.print()
    c.resize(5)
    c.print()
    print(c.area())
main()