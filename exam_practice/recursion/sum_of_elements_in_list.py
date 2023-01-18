from playsound import playsound
def sum_elements_in_list(listt):
    if type(listt) is int:
        return listt

    if len(listt) < 2:
        return sum_elements_in_list(listt[0])

    mid = len(listt) // 2

    return sum_elements_in_list(listt[:mid]) + sum_elements_in_list(listt[mid:])




lst = [1, 2, [3], [1, 2, 3], [[[[[[[6, 7, 8]]]]]]]]
print(sum_elements_in_list(lst))
playsound()