list1 = [12, 10, 15, 6, 7, 10, 19, 14]

def sum_between_first_last_odd(list1):
    first_odd = 0
    last_odd = 0
    for i in range(len(list1)):
        if list1[i] % 2 == 1:
            first_odd = i
            break

    for i in range(len(list1)-1, -1, -1):
        if list1[i] % 2 == 1:
            last_odd = i
            break

    sum = 0
    for i in range(first_odd, last_odd+1):
        sum += list1[i]
    return sum
print(sum_between_first_last_odd(list1))