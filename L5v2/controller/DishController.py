from L5v2.models.CookedDish import CookedDish

def add_new_dish(dishes: list[CookedDish], dish: CookedDish):
    """
    :param dishes: list of dishes
    :param dish: a dish to be appended
    :return: the new list
    """
    dishes.append(dish)
    return dishes

def update_dish(dishes: list[CookedDish]):
    """
    Updates a dish in the list
    """
    for i in range(len(dishes)):
        print(f"Index: {i}, Drink: {str(dishes[i])}")

    try:

        option = int(input("Choose the index of the drink to be updated: "))

        if option not in range(len(dishes)):
            return

        name = input("Enter a new name for th dish: ").strip()
        portion_size = int(input("Enter a new value for the portion sieze: ").strip())
        price = int(input("Enter a new value for the price: ").strip())
        preparation_time = int(input("Enter a new value for the preparation time").strip())

        new_dish = CookedDish(name = name, portion_size = portion_size, price = price, preparation_time = preparation_time)

        dishes[option] = new_dish

    except:
        return


def remove_dish(dishes: list[CookedDish]):
    """
    Removes a dish from the database
    """
    for i in range(len(dishes)):
        print(f"Index: {i}, Dish: {str(dishes[i])}")

    try:
        option = int(input("Choose the index of the drink to be removed"))

        dishes.pop(option)

    except:
        return None