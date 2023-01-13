from models.CookedDish import CookedDish


def add_new_dish(dishes: list[CookedDish], dish: CookedDish):
    """
    :param dish:  The dish to be appended to the list
    :param dishes: a list of dishes
    :return: The appended list
    """
    dishes.append(dish)

    return dishes


def update_dish(dishes: list[CookedDish]):
    """
    This function updates a specific dish in the list
    """
    for i in range(len(dishes)):
        print(f"Index: {i}, Drink: {str(dishes[i])}")

    try:
        """
        I know this is stupid but i am tired
        """

        option = int(input("Choose the index of the drink you want to update "))

        if option not in range(len(dishes)):
            return

        name = input("Enter a new name ").strip()
        portion_size = int(input("Enter a new portion size ").strip())
        price = int(input("Enter a new price ").strip())
        prep_time = int(input("Enter a new prep time ").strip())

        new_dish = CookedDish(name=name, portion_size=portion_size, price=price, prep_time=prep_time)

        dishes[option] = new_dish
    except:
        return


def remove_dish(dishes: list[CookedDish]):
    """
    This function removes a dish from the database
    """
    for i in range(len(dishes)):
        print(f"Index: {i}, Drink: {str(dishes[i])}")

    try:
        """
        I know this is stupid but i am tired
        """

        option = int(input("Choose the index of the drink you want to remove "))

        dishes.pop(option)
    except:
        return None
