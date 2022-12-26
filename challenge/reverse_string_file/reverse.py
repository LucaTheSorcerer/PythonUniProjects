from functools import reduce
# def reverse_File():
#     with open("challenge.txt") as f:
#         data = f.read()
#         data = data[::-1]
#
#     f = open("challenge.txt", "w")
#     f.write(data)
#     print(data)
# reverse_File()

filename = "challenge.txt"
print([line.strip() for line in open("challenge.txt")])
x = lambda line: [line.strip() for line in open("challenge.txt")]
print(x)




"""
Classic Method to find primes numbers in an n specified range, 1000 on this example is n
"""
# def isPrime(num: int) -> bool:
#     for n in range(2, int(pow(num, 0,5)+1)):
#         if num % n == 0:
#             return False
#     return True
#
# primes = []
# for number in range(2, 1000):
#     if isPrime(number):
#         primes.append(number)
#
#
# #One line
# print(list(filter(None, map(lambda y: y * reduce(lambda x, y: x * y != 0,
# map(lambda x, y = y : y % x, range(2, int(pow(y, 0.5) + 1))), 1), range(2, 100)))))

"""
    Third lambda checks the divisibility of y so it checks it the number y is prime
    Second lambda checks if the product of the numbers in the list is 0, and if it is then the numbers are not prime
    First lambda runs from 2 to the specified n number so up to that number it will output all primes, so y will take
values from 2 to the specifiesd n
    The reduce function will return True if the number is prime, False otherwise
    In Range (2, 100), 100 is the n number
"""
