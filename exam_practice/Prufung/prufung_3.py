def my_func(some_list, other_function):
    my_list = []
    for num in some_list:
        if other_function(num):
            my_list.append(num)
    return my_list



def recursive(some_list, other_function):
    my_list = []
    if len(some_list) == 0:
        return 0
    for num in some_list:
        if other_function(num):
            return my_list.append(num)  +  recursive(some_list, other_function)


# def replicate_recur(some_list, other_function):
#     result2 = []
#     if len(some_list) == 0:
#         result2.append(0)
#     else:
#         for num in some_list:
#             if other_function(num):
#               result2.append()
#               replicate_recur(times - 1, data)
#     return result2
def other_function():
    print("Wtf")


some_list = [1, 2, 3, 4, 5, 6]

def main():
    #print(my_func(some_list, other_function()))
    print(recursive(some_list, other_function()))
main()