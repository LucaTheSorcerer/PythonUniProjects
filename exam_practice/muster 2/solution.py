import operator
from functools import reduce
"""
Aufgabe 1
"""
import csv


def ub1(subject):
    with open("text.txt", 'r') as file:
        lines = file.readlines()
        lines = list(filter(lambda line: line.split(',')[2] == subject, lines))
        average_grade = reduce(lambda suma, line: suma + int(line.split(',')[3]), lines, 0) / len(lines)
        return average_grade


def correct_test_ub1():
    assert ub1("Advanced programming") == 8.166666666666666

def incorrect_test_ub1():
    pass
    #assert ub1("Advanced programming") == 3

def run_test():
    correct_test_ub1()
    incorrect_test_ub1()
"""
Aufgabe 2
"""

"""
Punkt A
"""
class NoMoney(Exception):
    pass
class BankAccount:
    def __init__(self, owner):
        self.amount = 0
        self.owner = owner

    def whitdraw(self, withdraw_number):
        if withdraw_number > self.amount:
            raise NoMoney("You don't have enough money!")

        return self.amount - withdraw_number

"""
Punkt B
"""
class CreditBankAccount(BankAccount):
    def __init__(self, owner):
        super().__init__(owner)
        self.credit_score = 1

    def whitdraw(self, withdraw_number):
        try:
            difference = super().whitdraw(withdraw_number)
            self.credit_score += 1
        except NoMoney:
            self.credit_score -= 1

        return difference

    def __add__(self, other):
        new_instance = CreditBankAccount(self.owner)
        new_instance.amount = self.amount + other.amount
        new_instance.credit_score = self.credit_score + other.credit_score
        return new_instance


"""
Aufgabe 3
"""
def my_func(n):
    if n in (0, 1):
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def recursive(n):
    if n in (0, 1):
        return n

    return recursive(n-1) + recursive(n-2)

def main():

    print(ub1("Advanced programming"))
    account1 = BankAccount("Luca")
    #print(account1.whitdraw(100))

    account2 = CreditBankAccount("Tudor")
    account2.amount = 30

    account3 = CreditBankAccount("Daniel")
    account3.amount = 20

    account4 = account2 + account3
    print(f"{account4.owner}{account4.amount}")

    print(my_func(5))
    print(recursive(5))

    run_test()
main()

