def sum(a, b):
    return a + b

"""
*args se foloseste pentru un numar variabil de argumente pozitionale
**kwargs se foloseste pentru un numar variabil de named parameters
"""

def f(**kwargs):
    print(type(kwargs))
    print(kwargs)

def g(*args):
    print(type(args))
    print(args)
def main():
    print(sum(1, 2)) #argumente pozitionale
    print(sum(a = 1, b = 2)) #named parameters

    f(a = 1, b = 2)

    g(1, 2)

    d = {'A':2, 'B':10}
    f(**d)
main()