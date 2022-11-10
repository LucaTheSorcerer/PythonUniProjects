number = int(input("Enter a number: "))
list1 = list(map(int, input("Enter a list ").strip().split()))

def check_sum_equal_number(number, list1):
    """
    This function checks if two consecutive numbers from the list are qual to the given number als paramter
    :param number: this is the given number that we check the sum with
    :param list1: this list contains all the numbers in our list
    :return: return True if the sum of two consecutive numbers are equal to the given number, False otherwise
    """
    for element1 in range(0, len(list1)-1):
        for element2 in range(element1+1, len(list1)):
            if list1[element1] + list1[element2] == number:
                return(element1, element2, list1[element1], list1[element2])
print(check_sum_equal_number(number, list1))



