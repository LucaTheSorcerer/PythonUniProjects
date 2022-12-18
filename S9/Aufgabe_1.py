import math

#Punkt A
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"



#Punkt B
class Circle:
    def __init__(self, x, y, r):
        self.c = Point(x,y)
        self.r = r

    #Punkt C
    def move(self, dx, dy):
        self.c.x += dx
        self.c.y += dy

    #Punkt D
    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 10

    def __str__(self):
        return f"Circle=(c={self.c}, r={self.r})"

    def __lt__(self, other):
        return self.area() < other.area()


#Punkt F
def move(c1, c2):
    while c1.c - c2.c > c1.r + c2.r:
        c1.move()
#Punkt E
def sort_circle(circles):
    #return circles.sort Nu functioneaza pentru ca sort nu returneaza nimic
    circles.sort(key=lambda circle : circle.area())
    circles.sort(key=lambda circle : circle.area(), reverse = True)



    #return sorted(circles)


class Student:
    def __init__(self, name):
        object.__setattr__(self, "name", name)
    def __setattr__(self, name, value):
        raise TypeError(f"Cannot set {name}")

    def __delattr__(self, name):
        raise TypeError(f"Cannot delete {name}")

def main():

    bob = Student('bob')
    #bob.name = 'dob'
    print(bob.name)
    p1 = Point(1,2)
    p2 = Point(2,3)

    d3 = p1 - p2

    print(d3)

    c = Circle(1, 2, 10)
    c.move(1, 2)
    print(c.area())
    print(c, '\n')

    sc = [Circle(1,2, 5), Circle(2, 3, 3), Circle(2, 2, 1)]
    sort_circle(sc)
    #sc = sort_circle([Circle(1,2, 5), Circle(2, 3, 3), Circle(2, 2, 1)])
    for circle in sc:
        print(circle)
main()

