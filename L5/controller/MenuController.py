from L5.ui.ui1 import *
from L5.modelle.CookedDish import CookedDish
from L5.modelle.Drink import Drink
from L5.repository.DataRepo import *


class MenuController:
    def __init__(self, cooked_dish_repo, drink_repo):
        self.__cooked_dish_repo = cooked_dish_repo
        self.__drink_repo = drink_repo

    def menu(self):
        """
        This function represents the main menu that manages the restaurant menu
        :return:
        """
        option = menu("Menu", ["Show all dishes and drinks", "Add dishes or drinks", "Update dishes and drinks",
                               "Remove dishes and drinks", "Return to the previous menu"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.menu()

        option = int(option)

        match option:
            case 1:
                self.__show_all_dishes_and_drinks()
            case 2:
                self.__add_dishes_and_drinks()
            case 3:
                self.__update_dishes_and_drinks()
            case 4:
                self.__remove_dishes_and_drinks()
            case 5:
                pass
            case other:
                invalid_message_to_display()
                self.menu()


    def __show_all_dishes_and_drinks(self):
        header("Menu", '=')

        cooked_dishes = self.__cooked_dish_repo.get_all()
        drinks = self.__drink_repo.get_all()

        cooked_dishes_text = "Cooked dishes"
        drinks_text = "Drinks"
        print("=" * 10 + f"{cooked_dishes_text}" + "=" * 10)
        for i in range(len(cooked_dishes)):
            print(f"{i + 1}. {cooked_dishes[i]}")

        print("=" * 10 + f"{drinks_text}" + "=" * 10)

        for i in range(len(drinks)):
            print(f"{i + 1}. {drinks}")

        print()
        print(header("Menu", "="))

    def __add_item(self):
        """
        This function's functionality is to add new cooked dishes
        or drinks to the menu
        :return:
        """
        option = menu("Add an items on the menu", ["Cooked Dish", "Drink", "Return to the previous menu"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__add_item()

        option = int(option)

        match option:
            case 1:
                self.__add_drink()
                self.__add_item()
            case 2:
                self.__add_cooked_dish()
                self.__add_item()
            case other:
                invalid_message_to_display()
                self.__add_item()


    def __add_cooked_dish(self):
        header("New Cooked Dish")
        name = input("Name of the dish: ")
        portion_size = input("Enter size of the portion: ")
        price = int(input("Price of the dish: "))
        preparation_time = int(input("Enter time for preparation: "))

        new_dish = CookedDish(name, portion_size, price, preparation_time)
        result = self.__cooked_dish_repo.add(new_dish) #Implement add function
        if result == ResultCheck.SUCCES:
            print(f'New cooked dish - {new_dish} - has been succesfully added to the data base!')
        elif result == ResultCheck.ALREADY_EXISTS:
            print(f"The cooked dish - {new_dish} - already exists!")
        footer("New Cooked Dish")


    def __add_drink(self):
        header("Add a new Drink")
        name = input("Enter the name of the drink: ")
        portion_size = int(input("Enter the size of the portion: "))
        price = int(input("Enter the price of the drink: "))
        alcohol_content = int(input("Enter how much alcohol the drink contains: "))

        new_drink = Drink(name, portion_size, price, alcohol_content)
        result = self.__drink_repo.add(new_drink) #Implement add function in DrinkRepo
        if result == ResultCheck.SUCCES:
            print(f"The drink - {new_drink} - has been succesfully added!")
        elif result == ResultCheck.ALREADY_EXISTS:
            print(f"The drink - {new_drink} - already exists!")
        footer("Add a new Drink")


    def __update_item(self):
        menu("Update an item (dish/drink) by index")

        option = menu("Update an item", ["Cooked Dish", "Drink", "Return to the previous page"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__update_item()

        option = int(option)

        match option:
            case 1:
                self.__update_cooked_dish()
                self.__update_item()
            case 2:
                self.__update_drink()
                self.__update_item()

            case 3:
                pass

            case other:
                invalid_message_to_display()
                self.__update_item()

        print("=" * 10 + "Update item in the data base" + "=" * 10)
    def __update_cooked_dish(self):
        cooked_dishes = self.__cooked_dish_repo.get_all()
        option = menu("Update cooked dish", cooked_dishes, "=")

        if not option.isnumeric():
            invalid_message_to_display()
            self.__update_cooked_dish()

        option = int(option)

        if option not in range(1, len(cooked_dishes) + 1):
            invalid_message_to_display()
            self.__update_cooked_dish()

        dish = cooked_dishes[option-1]
        print(f"The chosen dish to update is: {dish}")
        print("=" * 10 + "Update Dish' Information" + "=" * 10)
        name = input("Enter the new name of the dish")
        portion_size = int(input("Enter the new portion size of the dish"))
        price = int(input("Enter the new price of the dish"))
        preparation_time = int(input("Enter the new preparation time of the dish"))

        updated_dish = CookedDish(id_=0)

        if name != '':
            updated_dish.name = name

        if portion_size != '':
            updated_dish.portion_size = int(portion_size)

        if price != '':
            updated_dish.price = int(price)

        if preparation_time != '':
            updated_dish.preparation_time = int(preparation_time)

        result = self.__cooked_dish_repo.update(dish, updated_dish)

        if result == ResultCheck.SUCCES:
            print(f"The dish - {dish} - has been updated to - {updated_dish} -")
        elif result == ResultCheck.NOT_FOUND:
            print(f"The dish - {dish} - has not been found!")
    def __update_drink(self):
        pass


    def __remove_item(self):
        """
        This function is used to remove an item from the data base
        :return:
        """
        header("Remove item")
        option = menu("Item", ["Cooked Dish", "Drink", "Go back to the previous menu"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.__remove_item()

        option = int(option)

        match option:
            case 1:
                self.__remove_cooked_dish()
                self.__remove_item()

            case 2:
                self.__remove_drink()
                self.__remove_item()

            case 3:
                pass

            case other:
                invalid_message_to_display()
                self.__remove_item()


    def __remove_cooked_dish(self):
        cooked_dishes = self.__cooked_dish_repo.get_all()
        option = menu("Remove cooked dish from data base", cooked_dishes, "=")

        if not option.isnumeric():
            invalid_message_to_display()
            self.__remove_cooked_dish()

        option = int(option)

        if option not in range(1, len(cooked_dishes) + 1):
            invalid_message_to_display()
            self.__remove_cooked_dish()

        dish = cooked_dishes[option-1]
        result = self.__cooked_dish_repo.remove(dish) #Implement remove function

        if result == ResultCheck.SUCCES:
            print(f"The dish - {dish} - has been successfully removed!")
        elif result == ResultCheck.NOT_FOUND:
            print(f"The dish - {dish} - has not been found in the data base")


    def __remove_drink(self):
        drinks = self.__drink_repo.get_all()
        option = menu("Remove a drink from the data base", drinks, "=")

        if not option.isnumeric():
            invalid_message_to_display()
            self.__remove_drink()

        option = int(option)

        if option not in range(1, len(drinks) + 1):
            invalid_message_to_display()
            self.__remove_drink()

        drink = drinks[option-1]
        result = self.__drink_repo.remove(drink)

        if result == ResultCheck.SUCCES:
            print(f"The drink - {drink} - has been successfully removed!")
        elif result == ResultCheck.NOT_FOUND:
            print(f"The drink - {drink} - has not been found!")
