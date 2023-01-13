import math
from functools import reduce

class Student:
    def __init__(self, name, age = 20):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


def finds(students, student):
    for s in students:
        if s == student:
            return True
    return False

class Vector:
    def __init__(self, *data): #Se poate trimite un numar variabil de parametri
        self.elems = list(data)

    def __add__(self, other):
        return Vector(*(a + b for  a, b in zip(self.elems, other.elems)))

    def __sub__(self, other):
        return Vector(*(a - b for  a, b in zip(self.elems, other.elems)))

    def __neg__(self):
        return Vector(*(map(lambda x: -x, self.elems)))


    def __abs__(self):
        return math.sqrt(sum(map(lambda x: x**2, self.elems)))
        #return math.sqrt(reduce(lambda acc, x: acc+x**2, self.elems))


def main():
    bob = Student("bob")
    s = str(bob)
    #print(s, bob)
    #print(bob < Student('dob', 21))

    students = [bob, Student('dob', 21)]

    print(finds(students, Student('dob', 21))) #Obiectele din lista si cel trimis ca parametru sunt diferite in memorie ca referinta
    print(Student('bob', 21) in students)

    u = Vector(1, 2)
    v = Vector(1, 2, 3)

    l = (1, 2, 3)
    w = Vector(*l) #Vector(1, 2, 3) echivalent cu asta
    print(v.elems, type(v.elems))
    print((v+w).elems) # s = v + w // v.__add__(w).elems
    print((v-w).elems)

    print((-v).elems)
    print(abs(v))
main()