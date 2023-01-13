class MyException(Exception):
    pass

class T:
    def __init__(self, x):
        if x < 0:
            raise MyException("x cannot be < 0")
        #Sau assert x > 0

        self.x = x

try:
    t = T(-10)
except:
    print("hopa")

class A:
    def __init__(self):
        self.x = 10

    def f(self):
        print("A::f()")

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 100

    def f(self):
        super().f()
        print("B::f()")

    def magic(self):
        return self
a = A()
b = B()
print(a.x, b.x, b.y)
a.f()
b.f()

print(b == b.magic())

t = T(-10)
print(t.x)

