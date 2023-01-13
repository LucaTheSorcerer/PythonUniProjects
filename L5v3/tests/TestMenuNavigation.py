from L5v3.controller.MenuNavigation import main_menu
from L5v3.repository.CookedDishRepo import CookedDishRepo
from L5v3.repository.CustomerRepo import CustomerRepo
from L5v3.repository.DrinkRepo import DrinkRepo
from L5v3.repository.OrderRepo import OrderRepo

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")
order_repo = OrderRepo("orders.txt")

main_menu(customer_repo, dish_repo, drinks_repo, order_repo)
