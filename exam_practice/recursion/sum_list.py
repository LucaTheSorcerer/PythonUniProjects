def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

print("Boi")
print(sum_list([1, 2, 3]))
