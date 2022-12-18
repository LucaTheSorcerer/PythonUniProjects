import functools

from  L5.modelle.Identifiable import Identifiable
from functools import reduce

class Order(Identifiable):
    def __init__(self, customer_id, list_of_meals, list_of_drinks, total_price):
        # meals : [3, 6]
        # drinks : [5, 9]

        super().__init__()
        self.__customer_id = customer_id
        self.__list_of_meals = list_of_meals
        self.__list_of_drinks = list_of_drinks
        self.__total_price = total_price

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
        meal_prices = functools.reduce(self.sum_meal_prices, self.__list_of_meals)
        drink_prices = functools.reduce(self.sum_drink_prices, self.__list_of_drinks)
        self.__total_price = meal_prices + drink_prices

    def __create_invoice(self):
        invoice = "Invoice for client: " + clients_repo.get_by_id(self.__customer_id)
        meals = []
        for id in self.__list_of_meals:
            meals += meals_repo.get_by_id(id)

        for id in self.__list_of_drinks:
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