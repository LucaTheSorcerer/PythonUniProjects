from L5.modelle.CookedDish import CookedDish
from L5.modelle.Drink import Drink
from L5.modelle.Customer import Customer
from L5.modelle.Order import Order
from L5.repository.DataRepo import DataRepo
from L5.repository.CustomerRepo import CustomerRepo
from L5.repository.DrinkRepo import DrinkRepo
from L5.repository.OrderRepo import OrderRepo
from L5.repository.CookedDishRepo import CookedDishRepo
from L5.ui.ui1 import *

class OrderController:
    """
    This class includes the menu and all the methods for managing orders
    ToDO:
        -methods:
            -- menu
            -- show all orders
            -- add order
            -- remove an order
            -- select a customer
    """

    def __init__(self, customer_repo, order_repo, cooked_dish_repo, drink_repo):
        self.__customer_repo = customer_repo
        self.__order_repo = order_repo
        self.__cooked_dish_repo = cooked_dish_repo
        self.__drink_repo = drink_repo

    def menu(self):
        """
        Method used to manage the menu
        :return:
        """
        option = menu("Manage orders", ["Show all orders", "Add an order", "Remove an order",
                                        "Return to the previous menu"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.menu()

        option = int(option)

        match option:
            case 1:
                self.__show_all_orders()



    def __show_all_orders(self):
        header("All Orders", "=")
        orders = self.__order_repo.get_all()

        for item in range(len(orders)):
            customers = self.__customer_repo.find_by_ids(orders[item].customer_id)
            items = [*self.__drink_repo.find_by_ids(orders[item].item_ids),
                     *self.__cooked_dish_repo.find_by_ids(orders[item].item_ids)]
            print(f"{item + 1}. {orders[items].pprint(customers, items)}\n")

        print("=" * 10 + "Orders" + "=" * 10)

    def __add_order(self):
        customers = self.__customer_repo.get_all()
        dishes = self.__cooked_dish_repo.get_all()
        drinks = self.__drink_repo.get_all()
        print("=" * 10 + "New order" + "=" * 10)
        
        #item_ids = list(map(lambda a : a.id, items))

    def __remove_order(self):
        pass


