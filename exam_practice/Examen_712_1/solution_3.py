# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(lst):
    n = len(lst)
    total = 0
    for num in lst:
        total += num
    return total / n


def recursive(lst):
    n = len(lst)
    if len(lst) == 1:
        return lst[0]
    else:
        n = len(lst)
        return (lst[0] + (n-1) * recursive(lst[1:])) / n

def main():
    print(my_func([1, 2, 2]))
    print(recursive([1, 2, 2]))
main()