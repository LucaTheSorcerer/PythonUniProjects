from models.Drink import Drink


def add_new_drink(drinks: list[Drink], drink: Drink):
    """
    :param drink:  The drink to be appended to the list
    :param drinks: a list of drinks
    :return: The appended list
    """
    drinks.append(drink)

    return drinks


def update_drink(drinks: list[Drink]):
    """
    This function updates a specific drink in the list
    """
    for i in range(len(drinks)):
        print(f"Index: {i}, Drink: {str(drinks[i])}")

    try:
        """
        I know this is stupid but i am tired
        """

        option = int(input("Choose the index of the drink you want to update "))

        if option not in range(len(drinks)):
            return

        name = input("Enter a new name ").strip()
        portion_size = int(input("Enter a new portion size ").strip())
        price = int(input("Enter a new price ").strip())
        alcohol = int(input("Enter a new alcohol content ").strip())

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
        """
        I know this is stupid but i am tired
        """

        option = int(input("Choose the index of the drink you want to remove "))

        drinks.pop(option)
    except:
        return None
