import math
from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __sub__(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

@dataclass
class Circle:
    c: Point()
    r: int = 0


    def area(self):
        return math.pi * self.r**2

    def move(self, dx, dy):
        self.c.x += dx
        self.c.y += dy



def sort_circle(circles):
    circles.sort(key = lambda circle: circle.area())




def main():
    p1 = Point(1, 2)
    print(p1)

    p2 = Point(2, 3)

    d3 = p1 - p2
    print(d3)

    c1 = Circle(p1, 10)
    #c1 = Circle(Point(1, 2), 10)
    #c1 = Circle(Point(1, 2))
    print(c1)

    print(c1.area())
    c1.move(1, 2)
    print(c1.area())

    sc = [Circle(p1, 10), Circle(p2, 3), Circle(p1, 7)]
    sort_circle(sc)

    for circle in sc:
        print(circle)

main()


