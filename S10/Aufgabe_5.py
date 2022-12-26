"""
Schreiben Sie eine Funktion, die das größte Element einer Liste zurückgibt.
"""

def biggest_number_from_list(numbers_list):
    if len(numbers_list) == 0:
        return 0
    return max(numbers_list[0], biggest_number_from_list(numbers_list[1:]))
number_list = [1, 9, 135, 4, 78]
print(biggest_number_from_list(number_list))