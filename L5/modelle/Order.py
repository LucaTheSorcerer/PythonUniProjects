import functools
from datetime import datetime, timedelta

from  L5.modelle.Identifiable import Identifiable
from L5.modelle.CookedDish import CookedDish
from functools import reduce

class Order(Identifiable):
    def __init__(self, customer_id, list_of_meals_ids, list_of_drinks_ids, total_price, time_of_order):
        # meals : [3, 6]
        # drinks : [5, 9]

        super().__init__()
        self.__customer_id = customer_id
        self.__list_of_meals_ids = list_of_meals_ids
        self.__list_of_drinks_ids = list_of_drinks_ids
        self.__total_price = total_price
        self.__time_of_order = time_of_order

    def __eq__(self, other):
        return super().__eq__(other) and self.__customer_id == other.__customer_id \
            and self.__list_of_drinks_ids == other.__list_of_drinks_ids \
            and self.__list_of_meals_ids == other.__list_of_meals_ids

    def __str__(self):
        return super().__str__() + f", Customer-ID = '{self.__customer_id}', ++Items++, Total Price = '{self.__total_price}'"

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self.__customer_id = customer_id

    @property
    def list_of_meals_ids(self):
        return self.__list_of_meals_ids

    @list_of_meals_ids.setter
    def list_of_meals_ids(self, list_of_meals_ids):
        self.__list_of_meals_ids = list_of_meals_ids

    @property
    def list_of_drinks_ids(self):
        return self.__list_of_drinks_ids

    @list_of_drinks_ids.setter
    def list_of_drinks_ids(self, list_of_drinks_ids):
        self.__list_of_drinks_ids = list_of_drinks_ids

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price):
        self.__total_price = total_price

    @property
    def time_of_order(self):
        return self.__time_of_order

    @time_of_order.setter
    def time_of_order(self, time_of_order):
        self.__time_of_order = time_of_order

    def generate_time_of_order(self):
        """
        Method used to generate the exact time of the order
        :return: time of order
        """
        self.__time_of_order = datetime.now().isoformat()

    def generate_estimated_time_of_delivery(self, dishes : list[CookedDish]):
        """
        This function has the purpose of returning the estimated delivery time
        of the current order
        :param dishes: takes as input a list of dishes
        :return: estimated time of delivery
        """
        maximum_preparation_time = max(dishes, key=lambda dish: dish.preparation_time).preparation_time
        estimated_time_of_delivery = datetime.fromisoformat(self.__time_of_order) + timedelta(minutes=int(maximum_preparation_time))
        return estimated_time_of_delivery.isoformat()

    def sum_meal_prices(self, a, b):
        # a = id of a meal
        # b = id of another meal
        mealA = meal_repo.get_meal_by_id(a)
        mealB = meal_repo.get_meal_by_id(b)
        return mealA.price() + mealB.price()

    def sum_drink_prices(self, drink1, drink2):
        drinkA = drink_repo.get_drink_by_id(drink1)
        drinkB = drink_repo.get_drink_by_id(drink2)
        return drinkA.price() + drinkB.price()

    def calculate_cost(self):
        meal_prices = functools.reduce(self.sum_meal_prices, self.__list_of_meals_ids)
        drink_prices = functools.reduce(self.sum_drink_prices, self.__list_of_drinks_ids)
        self.__total_price = meal_prices + drink_prices

    def __create_invoice(self):
        invoice = "Invoice for client: " + clients_repo.get_by_id(self.__customer_id)
        meals = []
        for id in self.__list_of_meals_ids:
            meals += meals_repo.get_by_id(id)

        for id in self.__list_of_drinks_ids:
            meals += drinks_repo.get_by_id(id)

        invoice += map(lambda meal: f"{str(meal.name)} ........ {str(meal.price)}\n", meals)
        invoice += "Total price of the order " + str(self.__total_price)
        return invoice


    def print_invoice(self):
        print(self.__create_invoice())


# class Math:
#      @staticmethod
#      def sum(a,b):
#          return a + b

# m = Math()
# m.sum(1,2) # doar in python
# Math.sum(1,2)  # cum trebuie folosit
#
# class A:
#     def __init__(self, a, b):
#         self.a = a #A.a = 1
#         self.b = b #A.b
#
#
# a = A(1,2)