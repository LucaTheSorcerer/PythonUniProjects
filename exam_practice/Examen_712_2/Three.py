def my_func(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n = n // 2
    return result


def test_my_funct():
    for x in range(1, 100):
        for n in range(1, 10):
            assert x**n == my_func(x, n)


test_my_funct()


def recursive_exponential(x, n):
    if x in (0, 1):
        return x

    if n == 1:
        return x
    if n == 0:
        return 1

    return x * recursive_exponential(x, n - 1)


# print(my_func(2, 2))
print(recursive_exponential(15, 2))


def test_recursive_exponential():
    for x in range(0, 100):
        for n in range(1, 10):
            assert my_func(x, n) == recursive_exponential(x, n)


test_recursive_exponential()