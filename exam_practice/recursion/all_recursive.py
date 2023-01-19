"""
Factorial
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

"""
Fibonacci
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Binary Search
"""
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

"""
Merge Sort
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

"""
Tower of Hanoi
"""
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

"""
DFS 
"""
def DFS(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph, neighbor, visited)


"""
Quick Sort
"""
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)

"""
All Permutations of a string
"""
def permute(data, i, length):
    if i==length:
        print( "".join(data))
    else:
        for j in range(i,length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

"""
Sum of list
"""
def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


"""
Product of list
"""
def product_list(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product_list(lst[1:])

"""
Reverse a string
"""
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

"""
GCD - Greatest common divisior
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

"""
Power of a numbers
"""
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

