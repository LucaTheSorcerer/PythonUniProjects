from L5v3.controller.MenuNavigation import main_menu
from L5v3.models.CookedDish import CookedDish
from L5v3.models.Customer import Customer
from L5v3.models.Drink import Drink
from L5v3.models.Order import Order
from L5v3.repository.CookedDishRepo import CookedDishRepo
from L5v3.repository.CustomerRepo import CustomerRepo
from L5v3.repository.DrinkRepo import DrinkRepo
from L5v3.repository.OrderRepo import OrderRepo

customer_repo = CustomerRepo("repository/DataBase/customers.txt")
dish_repo = CookedDishRepo("repository/DataBase/dishes.txt")
drinks_repo = DrinkRepo("repository/DataBase/drinks.txt")
order_repo = OrderRepo("repository/DataBase/orders.txt")

drink = Drink(3, "Vodka", 450, 120, 95)

customer = Customer(0, "Mihai", "Str. Ciorilor")
customer_repo.save([customer])
dishes = [CookedDish(1, "Pizza", 450, 12, 25), CookedDish(1, "Ciorba de burta", 350, 24, 45)]

order = Order(2, customer.id, [dishes[0].id, dishes[1].id], [drink.id])

order.generate_bill(dishes, [drink])

customer_repo.save([customer])
dish_repo.save(dishes)
drinks_repo.save([drink])
order_repo.save([order])

"""
The files are initialised with the data
"""

main_menu(customerRepo=customer_repo, cookedDishRepo=dish_repo, drinkRepo=drinks_repo, orderRepo=order_repo)
