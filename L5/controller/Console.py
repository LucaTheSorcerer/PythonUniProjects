import sys

from L5.controller.CustomerController import CustomerController
from L5.controller.MenuController import MenuController
from L5.controller.OrderController import OrderController
from L5.repository.CookedDishRepo import CookedDishRepo
from L5.repository.CustomerRepo import CustomerRepo
from L5.repository.DrinkRepo import DrinkRepo
from L5.repository.OrderRepo import OrderRepo
from L5.ui.ui1 import menu, invalid_message_to_display

class Console:
    def __init__(self, database = "L5/repository/database"):
        self.__customerRepo = CustomerRepo(f"{database}/customers/customers.pickle")
        self.__drinkRepo = DrinkRepo(f"{database}/menu/drink.pickle")
        self.__cookedDishRepo = CookedDishRepo(f"{database}/menu/cooked_dish.pickle")
        self.__orderRepo =OrderRepo(f"{database}/orders/orders.pickle")
        self.customerController = CustomerController(self.__customerRepo)
        #self.__menuController = MenuController()
        #self.__orderController = OrderController()


    def main_menu(self):

        option = menu("Restaurant", ["Dishes", "Menu", "Customer", "Exit"])

        if not option.isnumeric():
            invalid_message_to_display()
            self.main_menu()

        option = int(option)

        match option:
            case 1:
                pass
            case 2:
                pass
            case 3:
                self.customerController.menu()
                self.main_menu()
            case 4:
                exit()
            case other:
                invalid_message_to_display()
                self.main_menu()