from L5v3.models.Drink import Drink


def add_new_drink(drinks: list[Drink], drink: Drink):
    """
    :param drink:  The drink to be added to the list
    :param drinks: list of drinks
    :return: The new list with the drink
    """
    drinks.append(drink)

    return drinks


def update_drink(drinks: list[Drink]):
    """
    This function updates a drink in the list with new parameters
    """
    for i in range(len(drinks)):
        print(f"Index: {i}, Drink: {str(drinks[i])}")

    try:

        option = int(input("Choose the index of your desired drink to be updated "))

        if option not in range(len(drinks)):
            return

        name = input("Enter a new name for your drink: ").strip()
        portion_size = int(input("Enter a new value for the portion size of your drink: ").strip())
        price = int(input("Enter a new value for the price of your drink ").strip())
        alcohol = int(input("Enter a new value for the alcohol content of your drink: ").strip())

        new_drink = Drink(name=name, portion_size=portion_size, price=price, alcohol=alcohol)

        drinks[option] = new_drink
    except:
        return None


def remove_drink(drinks: list[Drink]):
    """
    This function removes a drink from the database
    """
    for i in range(len(drinks)):
        print(f"Index: {i}, Drink: {str(drinks[i])}")

    try:

        option = int(input("Choose the index of the drink you want to remove "))

        drinks.pop(option)
    except:
        return None
