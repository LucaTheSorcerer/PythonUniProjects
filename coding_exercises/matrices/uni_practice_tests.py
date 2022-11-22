# # matrix = [
# #     [12, 6, 3, 0],
# #     [13, 7, 4, 1],
# #     [14, 8, 5, 2],
# #     [15, 10, 11, 9]
# # ]
#
#
#
#
# # def outer_square(matrix):
# #     new_list = []
# #
# #
# #     #First line:
# #     for i in range(len(matrix)):
# #         new_list.append(matrix[0][i])
# #
# #     #Last column
# #     for i in range(1, len(matrix)):
# #         new_list.append(matrix[i][len(matrix)-1])
# #
# #     #Last row revered
# #     for i in range(len(matrix)-2, -1, -1):
# #         new_list.append(matrix[len(matrix)-1][i])
# #
# #     #First column reversed
# #     for i in range(len(matrix)-2, 0, -1):
# #         new_list.append(matrix[i][0])
# #
# #     #Center square
# #
# #     return new_list
# # print(outer_square(matrix))
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]
#
#
# def spiral_matrix(matrix):
#     """
#     ToDo:
#         -split the matrix into parts
#         -with each iteration eliminate a row or a column
#     :param matrix:
#     :return:
#     """
#     starting_line_index = 0
#     ending_line_index = len(matrix)
#     starting_column_index = 0
#     ending_column_index = len(matrix[0])
#
#     while(starting_line_index < ending_line_index and starting_column_index < ending_column_index):
#
#         #Print first row from the remaining rows
#         for i in range(starting_column_index, ending_column_index):
#             print(matrix[starting_line_index][i])
#         starting_line_index += 1
#
#         #Print last column from the remaining columns
#         for i in range(starting_line_index, ending_line_index):
#             print(matrix[i][ending_column_index-1])
#         ending_column_index -= 1
#
#         #Print the last row from the remaining rows:
#         if (starting_line_index < ending_line_index):
#             for i in range(ending_column_index-1, starting_column_index-1, -1):
#                 print(matrix[ending_line_index-1][i])
#             ending_line_index -= 1
#
#         #Print the first column from the remaining columns:
#         if(starting_column_index < ending_column_index):
#             for i in range(ending_line_index -1, starting_line_index -1, -1):
#                 print(matrix[i][starting_column_index])
#             starting_column_index += 1
#
# spiral_matrix(matrix)
#
#
# """
# 2019 2. a)
# """
# m = []
# n = 3
# counter = 1
#
#
# for i in range(n):
#     linie = []
#     for j in range(counter+n-1, counter-1, -1):
#         linie.append(j)
#
#     m.append(linie)
#     counter += n
# print(m)
#
#
# """
# 2022 4. a)
# """
# #doi vectori a, b
# #vector a * b
#
# a = [1, 2, 3]
# b = [0, 5 ,3]
#
# c = [0, 10, 9]
#
# def f(a, b):
#     rezultat = []
#     lungime = min(len(a), len(b))
#     for i in range(lungime):
#         rezultat.append(a[i] * b[i])
#     return rezultat
#
# def f1(a,b):
#     return [a[i] * b[i] for i in range(min(len(a), len(b)))]
#
# def test():
#     assert f(a, b) == c
#     assert f1(a, b) == c
# test()
#
#
# """
# Muster_3 A2
# """
# def encode(instructiuni):
#     alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     pozitie_cursor = 0
#     rezultat = ''
#
#     for index, instructiune in enumerate(instructiuni):
#         if instructiune == ">":
#             pozitie_cursor += 1
#
#         if instructiune == "<":
#             pozitie_cursor -= 1
#
#         if instructiune == '+':
#             nr = 1
#             if len(instructiuni) > index + 1 and instructiuni[index+1].isdigit():
#                 nr = int(instructiuni[index+1])
#
#             rezultat += alfabet[pozitie_cursor] * nr
#
#         if instructiune == "|":
#             rezultat = rezultat[:-2]
#
#         if instructiune == '$':
#             rezultat += rezultat[-1]
#
#     return rezultat
#
#


dictionary = {
    "brand": "Ford",
    "year": 2023,
    "model": "Mustang"
}

x = ('key1', 'key2', 'key3')
y = 1
dictionaryy = dict.fromkeys(x, y)
dictionaryy.fromkeys(x, y)
dictionaryy.update({"key1": 2022})
del dictionaryy['key1']
print(dictionary)
print(dictionaryy)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tupple = (1, 2, 3)
list1.extend(list2)
print(list1)
list1.extend(tupple)
print(list1)
list1.remove(2)
print(list1)
list1.append("banana")
list1.insert(0, "watermelon")
list1[2:4] = ["banana"]
print(list1)

for element in list1:
    print(element)

for element in range(len(list1)):
    print(list1[element])

[print(x) for x in list1]
[print(key) for key in dictionary.keys()]

print("\n")
list2 = ["banana", "apple", "kiwi", "orange"]

for fruit in range(len(list2)):
    print(list2[fruit])

print("\n")

[print(list2[fruit]) for fruit in range(len(list2))]
print("\n")
list3 = [print(list2[fruit]) for fruit in range(len(list2)) if "a" in list2[fruit] and "o" in list2[fruit]]


fruit = ["banana", "apple", "appricot"]
new_list = [x for x in range(10) if x < 5]
new_list1 = [x.title() for x in fruit]
new_list2 = [fruit[element].upper() for element in range(len(fruit))]
new_list3 = ["hello" for element in fruit]

numbers_list = [100, 4, 3, 200, 567]
numbers_list.sort()
numbers_list.sort(reverse=True)

print(new_list)
print(new_list1)
print(new_list2)
print(new_list3)
print(numbers_list)

list4 = ["banana", "apple", "orange", "kiwi"]
set4 = {"banana", "apple", "orange", "kiwi"}
tuple4 = ("banana", "apple", "orange", "kiwi")
dict4 = {"1": "banana", "2": "apple", "3": "orange", "4":"kiwi"}
list4_string = " ".join(list4)
set4_string = " ".join(set4)
tuple4_string = " ".join(tuple4)
dict4_string = " ".join(dict4.values())
print(list4_string)
print(set4_string)
print(tuple4_string)
print(dict4_string)

string2 = "ABCD"
#replaced_string = string2.replace("A", list4[0])
replaced_string = ""
for i in range(len(string2)):
    replaced_string += string2.replace(string2[i], list4[0])
print(replaced_string)

list5 = ["apple", "banana"]
list6 = ["orange", "kiwi"]
list5.extend(list6)
joined_string = " ".join(list5)
print(joined_string)

string3 = "abcd efg hij"
string3.strip()
print(string3)
split_string = string3.split(" ")
print(split_string)
print(split_string[0])

new_list4 = []
for word in split_string:
    letters = word.split(" ")[0]
    for letter in letters:
        new_list4.append(letter)

print(new_list4)


tuple_test = ("kiwi",)
print(type(tuple_test))


# for keys in dictionary.keys():
#     print(keys)
#
# for values in dictionary.values():
#     print(values)

# for key, values in dictionary.items():
#     print(f'{key} : {values}')
#
# my_dicitonary = dictionary.copy()
# print(my_dicitonary)
#
#
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
#
# for key, values in myfamily.items():
#     print(key)
#     print(values)

#
# for i in myfamily:
#     print(myfamily[i].items())


"""
Print matrix diagonally downwards
"""

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

"1 2 4"
def print_matrix_diagonally_downwards(matrix1):

    starting_row_index = 0
    endig_row_index = len(matrix1)
    starting_column_index = 0
    ending_columns_index = len(matrix1[0])

    result = []

    #I. Printing elements above and on second diagonal
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if i + j < len(matrix1) - 1:
                result.append(matrix1[i][j])

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if i + j == len(matrix1) - 1:
                result.append(matrix1[i][j])

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if i + j > len(matrix1) - 1:
                result.append(matrix1[i][j])

    return result
print(print_matrix_diagonally_downwards(matrix1))

def test():
    input = print_matrix_diagonally_downwards(matrix1)
    output = [1, 2, 4, 3, 5, 7, 6, 8, 9]
    assert input == output
    assert input == output
test()

"""
Print matrix elements from top-left to bottom right in diagonally upward manner
"""

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def printDiagonalTraversal(matrix2):

    max_size = len(matrix2)

    result = []
    for i in range(len(matrix2)):
        if max_size < len(matrix1[i]):
            max_size = len(matrix1[i])

    v = [[] for i in range(2 * max_size - 1)]

    for i in range(len(matrix2)):
        for j in range(len(matrix2)):
            v[i+j].append(matrix2[i][j])

    for i in range(len(v)):
        v[i] = v[i][::-1]

        for j in range(len(v[i])):
            print(v[i][j], end = "")

printDiagonalTraversal(matrix2)
print("\n")


#Minimum numbers of steps to convert a given into a Diagonally Dominant
#Matrix

matrix3 = [
    [3, -2, 1],
    [1, -3, 2],
    [-1, 2, 4]
]

def isDDM(matrix3):
    for i in range(len(matrix3)):
        sum = 0
        for j in range(len(matrix3)):
            sum += abs(matrix3[i][j])

        sum -= abs(matrix3[i][i])

        if(abs(matrix3[i][i]) < sum):
            return False

    return True
print(isDDM(matrix3))
