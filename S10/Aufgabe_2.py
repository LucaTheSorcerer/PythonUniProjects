"Schreiben Sie eine Funktion, die den letzten " \
"erhaltenen Großbuchstabe der Zeichenkette zurückgibt."
def return_last_uppercase_letter(list_of_letters):
    if len(list_of_letters) == 0:
        return 0
    return list_of_letters[-1] if list_of_letters[-1].isupper() else return_last_uppercase_letter(list_of_letters[-1-1])


def last_capital():
    pass

list_of_letters = ["a", "B", "c", "q", "a"]
print(return_last_uppercase_letter(return_last_uppercase_letter(list_of_letters)))