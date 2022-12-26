"Schreiben Sie für einegegebene Zeichenkette eine Funktion,die die Gesamtzahl der darinenthaltenen Vokalen (a, e, i, o und u) zählt."

def return_total_vocals(list_of_letters):

    vocals = ["a", "e", "i", "o", "u"]
    if len(list_of_letters) == 0:
        return 0
    return (1 if list_of_letters[0] in "aeiouAEIOU" else 0) + return_total_vocals(list_of_letters[1:])

list_of_letters = ["u", "e", "b"]
print(return_total_vocals("Assembly"))