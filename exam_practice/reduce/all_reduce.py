from functools import reduce

"""
Sum list
"""
def sum_list():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    print(total) # prints 15

"""
Prod list
"""
def prod_list():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x * y, numbers)
    print(total) # prints 15


"""
Max value in List
"""
def product_list():
    numbers = [1, 2, 3, 4, 5]
    maximum = reduce(lambda x, y: x if x > y else y, numbers)
    print(maximum) # prints 5

"""
Min value in list
"""
def min_value():
    numbers = [1, 2, 3, 4, 5]
    minimum = reduce(lambda x, y: x if x < y else y, numbers)
    print(minimum) # prints 1

"""
Concatenating list of strings
"""
def concate():
    strings = ["Hello", "World", "!"]
    sentence = reduce(lambda x, y: x + " " + y, strings)
    print(sentence) # prints "Hello World !"

