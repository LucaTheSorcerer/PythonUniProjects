from L5v3.controller.CustomerController import search_customer
from L5v3.models.Customer import Customer
from L5v3.models.Dish import Dish
from L5v3.models.Drink import Drink
from L5v3.models.Order import Order


def add_order(orders: list[Order], dishes: list[Dish], drinks: list[Drink], customers: list[Customer]):
    """
    This function manages everything about orders
    :param orders: A list with all the orders
    :param dishes: A list with all the dishes
    :param drinks: A list with all the drinks
    :param customers: A list with all the customers
    """

    customer = search_customer(customers)

    if customer is None:
        print("Add your customer to the list, first")
        return

    dish_IDs = []
    drink_IDs = []

    while True:
        print("Press 1 to add a dish")
        print("Press 2 to add a drink")
        print("Press 3 to finish the order")
        print("Press 4 to see the current items in the order")
        print("Press 5 to exit")

        option = int(input("Your option: "))

        if option == 1:
            for i in range(len(dishes)):
                print(f"Index: {i}, Dish: {str(dishes[i])}")

            try:


                option = int(input("Choose the index of your desired drink that you want to update "))

                if option not in range(len(dishes)):
                    continue

                dish_IDs.append(dishes[option].id)
            except:
                continue
        elif option == 2:
            for i in range(len(drinks)):
                print(f"Index: {i}, Drink: {str(drinks[i])}")

            try:


                option = int(input("Choose the index of your desired drink that you want to update "))

                if option not in range(len(drinks)):
                    continue

                drink_IDs.append(drinks[option].id)
            except:
                continue

        elif option == 3:
            break
        elif option == 4:
            print(dish_IDs)
            print(drink_IDs)
        elif option == 5:
            return
        else:
            pass

    order = Order(customer_id=customer.id, drinks_ids=drink_IDs, dish_ids=dish_IDs)
    orders.append(order)
    print(order)

    order.show_bill(dishes, drinks)
    print(f"The estimated time for your order is: {order.generate_estimated_wait_time(dishes)}")
