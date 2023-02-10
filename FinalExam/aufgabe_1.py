class PointName:
    def __init__(self, name):
        self.name = name

class Point(PointName):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point=({self.name},{self.x},{self.y})"

    def __repr__(self):
        return f"Point=({self.x}, {self.y})"

    def __add__(self, delta):
        return Point(self.name, self.x + delta, self.y + delta)

    def __sub__(self, sigma):
        return Point(self.name, self.x - sigma, self.y-sigma)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __ne__(self, other):
        return self.name == other.name




class Metaclass(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return super(Metaclass, cls).__new__(cls, clsname, superclasses, attributedict)



class MyClass(metaclass=Metaclass):
    pass
def main():
    p1 = Point("Point1", 1, 3)
    p2 = Point("Point2", 2, 2)
    p3 = Point("Point3", 3, 1)
    p2 = p2 + 10
    p2 = p2 - 5

    points = [p1, p2, p3]
    print(points)
    print(p1)
    print(p2)
    print(p1 == p2)

    print(p1.x < p2.x and p1.y < p2.y)
    print(p1 == p2)




    c = Metaclass('C', (object, ), {})
    print("class type: ", type(c))
    print(type(MyClass))
main()