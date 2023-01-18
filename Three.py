def my_func(lst):
    n = len(lst)
    total = 0
    for num in lst:
        total += num
    return total / n


def average(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        n = len(lst)
        return (lst[0] + (n - 1) * average(lst[1:])) / n