from L5v3.models.CookedDish import CookedDish


def add_new_dish(dishes: list[CookedDish], dish: CookedDish):
    """
    :param dish:  The dish to be added to the list
    :param dishes: list of dishes
    :return: list with the new dish
    """
    dishes.append(dish)

    return dishes


def update_dish(dishes: list[CookedDish]):
    """
    This function updates a dish with the new parameters
    """
    for i in range(len(dishes)):
        print(f"Index: {i}, Drink: {str(dishes[i])}")

    try:

        option = int(input("Choose the index of your desired dish to update: "))

        if option not in range(len(dishes)):
            return

        name = input("Enter a new name for your dish: ").strip()
        portion_size = int(input("Enter a new value for the portion size of your dish: ").strip())
        price = int(input("Enter a new value for the price of your dish: ").strip())
        prep_time = int(input("Enter a new value for the preparation time of your dish: ").strip())

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

        option = int(input("Choose the index of your desired dish to be removed: "))

        dishes.pop(option)
    except:
        return None
