from L5v2.controller.CustomerController import add_new_customer, search_customer, update_customer, remove_customer
from L5v2.controller.DishController import remove_dish, update_dish, add_new_dish
from L5v2.controller.DrinkController import remove_drink, update_drink, add_new_drink
from L5v2.controller.OrderController import add_order
from L5v2.models.CookedDish import CookedDish
from L5v2.models.Drink import Drink
from L5v2.repository.CookedDishRepo import CookedDishRepo
from L5v2.repository.CustomerRepo import CustomerRepo
from L5v2.repository.DrinkRepo import DrinkRepo
from L5v2.repository.OrderRepo import OrderRepo
from L5v2.ui.CustomerControllerUI import add_new_customer_input
from L5v2.ui.RestaurantMenu import RestaurantMenu
from L5v2.ui.UserMenu import print_starting_menu

def main_menu(customerRepo, cookedDishRepo, drinkRepo, orderRepo):
    """
    central loop of the program
    when this function breaks, the whole program stops executing
    :param customerRepo: customerrepo with its file path
    :param cookedDishRepo: cookeddishrepo with its file path
    :param drinkRepo: drinkrepo with its filepath
    :param orderRepo: orderrepo with its filepath
    :return:
    """

    while True:
        customers = customerRepo.load()
        dishes = cookedDishRepo.load()
        drinks = drinkRepo.load()
        orders = orderRepo.load()

        resturant_menu = RestaurantMenu(dishes, drinks)

        print_starting_menu()

        option = int(input("Enter your desired option: ").strip())
        print("\n")

        if option == 1:
            print(resturant_menu)

        elif option == 2:
            add_order(orders, dishes, drinks, customers)

        elif option == 3:
            print("Enter the details of the dish to add: ")
            try:
                name = input("Enter a new name ").strip()
                portion_size = int(input("Enter a new value for the portion size ").strip())
                price = int(input("Enter a new value for the price: ").strip())
                preparation_time = int(input("Enter a new value for the preparation time: ").strip())

                new_dish = CookedDish(name=name, portion_size=portion_size, price=price, preparation_time=preparation_time)

            except:
                continue

            add_new_dish(dishes, new_dish)

        elif option == 4:
            update_dish(dishes)

        elif option == 5:
            remove_dish(dishes)

        elif option == 6:
            print("Enter the details of the drink you want to add: ")

            try:
                name = input("Enter a new name ").strip()
                portion_size = int(input("Enter a new value for the portion size ").strip())
                price = int(input("Enter a new value for the price: ").strip())
                alcohol_content = int(input("Enter a new value for the alcohol content: ").strip())
                new_drink = Drink(name=name, portion_size=portion_size, price=price, alcohol_content=alcohol_content)

            except:
                continue

            add_new_drink(drinks, new_drink)

        elif option == 7:
            update_drink(drinks)

        elif option == 8:
            remove_drink(drinks)

        elif option == 9:
            customer = add_new_customer_input()
            customers = add_new_customer(customers, customer)

        elif option == 10:
            print("Search for the customer you want to update" + "\n")
            customer = search_customer(customers)

            if customer is None:
                continue

            name = input("Enter a new name: ").strip()
            address = input("Enter a new address: ").strip()

            if name == "":
                name = None

            if address == "":
                address = None

            update_customer(customers, customer, name, address)

        elif option == 11:
            print("Search for the customer you want to remove" + "\n")
            customer = search_customer(customers)

            if customer is None:
                continue

            remove_customer(customers, customer)

        elif option == 12:
            return

        else:
            pass

        customerRepo.save(customers)
        cookedDishRepo.save(dishes)
        drinkRepo.save(drinks)
        orderRepo.save(orders)