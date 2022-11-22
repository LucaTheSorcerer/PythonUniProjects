list1 = [2, 8, 6, 10, 8]

def check_if_odd(list):
    for i in range(len(list)):
        if list[i] % 2 == 1:
            return True
    return False

print(check_if_odd(list1))