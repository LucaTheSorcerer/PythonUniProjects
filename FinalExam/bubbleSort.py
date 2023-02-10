array = [1, 0, -9, 120, 420, 69, 42069, -27]

def bubble_sort(array):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                sorted = False

    return array

def bubble_sort_recursive(array):
    counter = 0


    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            array[i], array[i-1] = array[i-1], array[i]
            counter += 1

    if counter == 0:
        return array
    else:
        return bubble_sort(array)



def main():
    print(bubble_sort(array))
    print(bubble_sort_recursive(array))
main()

