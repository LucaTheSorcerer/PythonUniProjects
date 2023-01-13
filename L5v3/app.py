from controller.MenuNavigation import main_menu
from models.CookedDish import CookedDish
from models.Customer import Customer
from models.Drink import Drink
from models.Order import Order
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo

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
We initialise the files with data
"""

main_menu(customerRepo=customer_repo, cookedDishRepo=dish_repo, drinkRepo=drinks_repo, orderRepo=order_repo)
