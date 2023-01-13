from functools import reduce


class RestaurantMenu:
    def __init__(self, dishes, drinks):
        self.drinks = drinks
        self.dishes = dishes

    def __generate_menu(self):
        """
        :return: All the items on the menu as a string
        """
        menu_lines = [f"{index + 1}.'{item.name}'...'{item.price}'" for index, item in
                      enumerate(self.dishes + self.drinks)]
        return reduce(lambda s1, s2: s1 + "\n" + s2, menu_lines)

    def update_menu(self, dishes, drinks):
        """
        This function is deprecated probably
        Used to update the menu when an item is added or deleted
        """
        self.dishes = dishes
        self.drinks = drinks

    def __str__(self):
        return self.__generate_menu()
