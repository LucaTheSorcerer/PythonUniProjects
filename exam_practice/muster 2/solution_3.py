from functools import reduce


def my_func(n):
    if n in (0, 1):
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacii(n):
    if n in (0, 1):
        return n
    return fibonacii(n-1) + fibonacii(n-2)

def fibonacii_one_liner(n):
    one_line = lambda n: n if n in (0,1) else fibonacii_one_liner(n-1) + fibonacii_one_liner(n-2)
    return one_line

one_liner = lambda n: n if n in (0,1) else one_liner(n-1) + one_liner(n-2)

def main():
    print(my_func(4))
    print(fibonacii(4))
    #print(fibonacii_one_liner(4))
    print(one_liner(4))
main()

# f(4) : f(3) + f(2) = 2 + 1 = 3
# f(3): f(2) + f(1) = 1 + 1 = 2
#f(2): f(1) + f(0) = 1 + 0 = 1
#f(1): 1
#f(0): 0