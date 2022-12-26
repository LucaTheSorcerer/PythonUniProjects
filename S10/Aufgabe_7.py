"""

"""
from S10.Aufgabe_6 import *

def sum_list(l):
    s = 0
    for el in l:
        if type(el) is list:
            s += sum_list(el)

        else:
            s += el

    return s

def sum_list_v2(l):
    if type(l) is int:
        return l

    if len(l) < 2:
        return sum_list_v2(l[0])



    mid = len(l) // 2

    return sum_list_v2(l[:mid]) + sum_list_v2(l[mid:])

print(sum_list([1, 2, 3, [[[[[1, 2, 3]]]]]]))
print(sum_list_v2([1, 2, 3, [[[[[1, 2, 3]]]]]]))