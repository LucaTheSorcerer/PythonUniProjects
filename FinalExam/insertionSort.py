array = [1, 0, -9, 120, 420, 69, 42069, -27]

def insertion_sort(array):

    for i in range(1, len(array)):
        idx = i - 1
        element = array[i]

        while idx >= 0 and element < array[idx]:
            array[idx + 1] = array[idx]
            idx = idx - 1
        array[idx + 1] = element

    return array

def insertion_sort_recursive(array):
    counter = 0

    for i in range(1, len(array)):
        idx = i - 1
        element = array[i]

        while idx >= 0 and element < array[idx]:
            array[idx + 1] = array[idx]
            idx = i - 1
            counter += 1
        array[idx + 1] = element

    if counter == 0:
        return array
    else:
        return insertion_sort_recursive(array)

def main():
    print(insertion_sort(array))
    print(insertion_sort_recursive(array))
main()