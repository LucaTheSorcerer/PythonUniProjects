from controller.MenuNavigation import main_menu
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")
order_repo = OrderRepo("orders.txt")

main_menu(customer_repo, dish_repo, drinks_repo, order_repo)
