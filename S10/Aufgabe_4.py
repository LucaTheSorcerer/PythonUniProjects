"""
Schreiben Sie für eine Zahl eine Funktion,die true zurückgibt,wenn die angegebene Zahl Palindrom ist,andernfalls falsch.
"""
import math


def check_palindrome(number):
    return len(number) < 2 or number[0] == number[-1] and check_palindrome(number[1:-1])

print(check_palindrome("1331"))

def palindrome(n):
    if n < 10:
        return False
    if n % 10 != n//10**(int(math.log10(n))):
        return False
    return palindrome(n//10 % (10**(int(math.log10(n)))))

print(palindrome(121))