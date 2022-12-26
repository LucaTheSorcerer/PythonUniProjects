def header(title, symbole = '='):
    print()
    print(symbole * len(title) + title + symbole * (len(title)))


def footer(title, symbole = '='):
        print(symbole * len(title))

def invalid_message_to_display():
    print(f"Your option is not a valid one")


def menu(title, options, symbole = '='):
    header(title, symbole)

    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    footer(title, symbole)

    return input("Choose valid option from above")