from L5v2.models.Drink import Drink

def add_new_drink(drinks: list[Drink], drink: Drink):
    """
    :param drinks: list of drinks
    :param drink: drink to be added to the list
    :return: the new list
    """
    drinks.append(drink)
    return drinks

def update_drink(drinks: list[Drink]):
    """
    updates a drink in the list
    :param drinks:
    :return:
    """

    for i in range(len(drinks)):
        print(f"Index: {i}, Drink: {str(drinks[i])}")

    try:
        option = int(input("Choose the index of the drink to be updated: "))

        if option not in range(len(drinks)):
            return

        name = input("Enter a new name for the drink: ").strip()
        portion_size = int(input("Enter a new value for the portion size: ").strip())
        price = int(input("Enter a new price for the drink: ").strip())
        alcohol_content = int(input("Enter a new value for the alcohol content: ").strip())

        new_drink = Drink(name=name, portion_size=portion_size, price=price, alcohol_content=alcohol_content)

        drinks[option] = new_drink

    except:
        return None

def remove_drink(drinks: list[Drink]):
    """
    Removes a drink from the databse
    """
    for i in range(len(drinks)):
        print(f"Index: {i}, Drink: {str(drinks[i])}")

    try:
        option = int(input("Choose the index of the drink to be removed: "))

        drinks.pop(option)

    except:
        return None
