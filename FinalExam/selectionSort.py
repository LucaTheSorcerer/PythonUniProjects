array = [1, 0, -9, 120, 420, 69, 42069, -27]

def selection_sort(array):

    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[j], array[i] = array[i], array[j]

    return array

def selection_sort_recursive(array):
    counter = 0
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                counter += 1
    if counter == 0:
        return array
    else:
        return selection_sort_recursive(array)


def main():
    print(selection_sort(array))
    print(selection_sort_recursive(array))
main()
