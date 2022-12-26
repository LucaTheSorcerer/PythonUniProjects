"""
Schreiben Sie eine Funktion, die prüft, ob eine Zahl in einer Liste erhalten ist.
Jedes Element kann entweder eine Liste oder eine Zahl sein.
"""

def check_if_element_in_list(elements_list, c):
    for el in elements_list:
        if type(el) is list:
            if check_if_element_in_list(el, c):
                return True

        if el == c:
            return True
    return False

print(check_if_element_in_list([1, 2, 3, [[[[[1, 2, 3]]]]]], 3))