class Data:
    def __init__(self):
        self.data = []

    def add_element(self, elem):
        self.data.append(elem)

    def print_elements(self):
        for el in self.data:
            print(el)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

data = Data()

for i in range(10):
    data.add_element(i)

print(data[1])

print("second element", data[1])

data[1] = 101 #data.__setitem__(1,101)

data.print_elements()


class R:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError("b cannot be 0")

        if isinstance(a, int) and isinstance(b, int):
            self.__a = a
            self.__b = b

        else:
            raise ValueError("args should be int")


    def __add__(self, o):
        return R(self.a*o.b + self)



#Ubung
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        pass

    def eat(self):
        pass

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __add__(self, other):
        return Student(self.name, self.age + other)

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"
def main():
    bob = Student('bob', 20)
    print(bob + 10)

    print(bob > bob + 10)

    students = [bob + 5, bob, bob + 3, bob + 2]

    students.sort()
    students.sort(key=lambda student: student.age, reverse=True)

    from operator import attrgetter
    students.sort(key=attrgetter('age'), reverse=True)


    print(students)
main()

#Data CLASS
red = (255, 0, 0)
green = 0, 255, 0
white = tuple(255, 255, 255)

red1 = list((255, 0, 0))
green1 = [255, 0, 0]


red2 = dict(red = 255, green = 0, blue = 0)

from collections import namedtuple

Color = namedtuple('Color', 'red green blue')
red3 = Color(255, 0, 0)
green3 = Color(red = 0,
               green = 255,
               blue = 0)
#green.red functioneaza
#pentru ca e tuple, nu se poate schimba valoarea si trebuie grija cu ordinea elemenetelor


from typing import NamedTuple

class Color(NamedTuple):
    red : int
    green: int
    blue: int = 0 #default

red4 = Color(255, 0)


from types import SimpleNamespace

red5 = SimpleNamespace(red=255, green=0, blue=0) #ca un dicitionar
#red5.red functioneaza

class Color1:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

red6 = Color1(255, 0, 0)
green4 = Color1(red = 0,
               green = 255,
               blue = 0)
#green4.red functioneaza!


"""
DATACLASS
"""

from dataclasses import dataclass

@dataclass #dataclass implementeaza singura toate metodele de mai sus, si reduce clasa, daca
            #daca se pune dataclass(order = True) sorteaza elementele
class Color3:
    red: int
    green: int
    blue: int


from dataclasses import make_dataclass