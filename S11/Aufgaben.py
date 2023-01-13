"""
Aufgabe 1: Schreiben Sie eine Funktion, die zwei sortierte Listen zu einer sortierten Liste zusammenführt.
"""

def inter(left, right):
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    l += left[i:]
    l += right[j:]
    # while i < len(left):
    #     l.append(left[i])
    #
    # while j < len(right):
    #     l.append(right[i])

    return l

"""
Aufgabe 2: Gegeben sei eine Liste bestehend aus 0 und 1. Schreiben Sie eine rekursive Funktion, die eine solche Liste
           sortiert. Die Funktion sollte zuerst alle 0, dann alle 1 setzen.
"""

def sort10(l):
    if len(l) < 1:
        return l

    if l[0] == 0:
        return [0] + sort10(l[1:])

    return sort10(l[1:]) + [1]

"""
Aufgabe 3: Schreiben Sie eine Funktion, die das kleinste fehlende Element aus einer sortierten Liste findet.
"""

def missing(l, start, end):

    if start > end:
        return end + 1

    if start != l[start]:
        return start

    mid = (start + end) // 2

    if mid == l[mid]:
        return missing(l, mid + 1, end) #Toate elementele de dinainte sunt deja sortate daca mid == l[mid]

    return missing(l, start, mid) #sau mid-1


"""
Aufgabe 4 : Gegeben sei eine sortierte Liste. Schreiben Sie eine Funktion, die ein Triplett aus der Liste bestimmt, das
            sich zu einem bestimmten Wert summiert.
"""

def triple(l, target):
    for i, start in enumerate(l):
        target -= start

        a = i + 1
        b = len(l) - 1

        while a < b:
            s = l[a] + l[b]

            if s == target:
                return start, l[a], l[b]
            elif s < target:
                a += 1
            else:
                b -=1

    return None


def find3Numbers(A, arr_size, sum):
    A.sort()

    for i in range(0, arr_size - 2):
        l = i + 1
        r = arr_size - 1
        while l < r:
            if(A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i], A[l], A[r])
                return True
            elif A[i] + A[l] + A[r] < sum:
                l += 1
            else:
                r -= 1 #A[i] + A[l] + A[r] > sum

    return False

"""
Aufgabe 5: Schreiben Sie eine Funktion, die die Anzahl von 1 in einer sortierten Liste zurückgibt.
"""

def find_all_1(l1, number):
    if len(l1) == []:
        return 0

    counter = 0

    for i in l1:
        if i == number:
            counter += 1
    return counter

def find_all_1_recursive(lst, key):
    if lst == []:
        return 0
    if lst[0] == key:
        return 1 + find_all_1_recursive(lst[1:], key)
    else:
        return 0 + find_all_1_recursive(lst[1:], key)

"""
Aufgabe 6: Schreiben Sie eine Funktion, die den Index des letzten Vorkommen eines bestimmten Elements zurückgibt.
"""

def find_last_index_element(l2, n, c = None):
    if c is None:
        c = len(l2) - 1
    if c < 0:
        return -1
    elif l2[c] == n:
        return c
    else:
        return find_last_index_element(l2, n, c-1)

"""
Aufgabe 7: Bucketsort ist ein Sortierverfahren, das für bestimmte Werte-Verteilungen eine Eingabeliste in linearer Zeit
           sortiert. Der Algorithmus ist in drei Phasen eingeteilt:
                ● Verteilung der Elemente auf die Buckets (Partitionierung)
                ● Jeder Bucket wird mit einem weiteren Sortierverfahren wie beispielsweise Mergesort sortiert.
                ● Der Inhalt der sortierten Buckets wird konkateniert.
Implementieren Sie den Bucketsort in Python.
"""

def bucketsort(array):

    #Create empty buckets
    bucket = []
    for i in range(len(array)):
        bucket.append([])

    #Insert elements in the buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    #Sort elements in each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    #Get the sorted elements from all buckets
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1

    return array

"""
Aufgabe 8: Implementieren Sie eine Funktion get_column, die eine Zahl i, eine Zahl N und einen String m als Argument
           bekommt. Der String repräsentiert eine NxN-Matrix mit Zeichen. Die Funktion soll die i-te Spalte der Matrix
           m zurückgeben.
           
           Die Methode soll ValueError auslösen, wenn m keine NxN-Matrix repräsentiert. Der String enthält nur
           Zeichen.
"""


def main():
    a = [1, 7, 8, 10]
    b = [2, 6, 11]

    l = [1, 0, 0, 1, 1, 0, 0, 0]

    p = [0, 1, 2, 3, 4]

    print(inter(a, b))
    print(sort10(l))
    print(missing(p, 0, 4))
    sum = 6
    arr_size = len(p)
    print(find3Numbers(p, arr_size, sum))
    print(triple(p, 6))

    l1 = [0, 5, 1, 9, 1, 10, 1]
    l2 = [0, 5, 1, 40, 2, 1, 9]
    print(find_all_1(l1, 1))
    print(find_all_1_recursive(l1, 1))

    print(find_last_index_element(l2, 1))

    array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted array in descending order is: ")
    print(bucketsort(array))
main()


