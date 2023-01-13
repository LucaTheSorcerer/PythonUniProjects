from L5v2.models.CookedDish import CookedDish
from L5v2.models.Customer import Customer
from L5v2.models.Order import Order
from L5v2.repository.CookedDishRepo import CookedDishRepo
from L5v2.repository.CustomerRepo import CustomerRepo
from L5v2.repository.DrinkRepo import DrinkRepo
from L5v2.repository.OrderRepo import OrderRepo

"""
Tests the functionalities of Order class and OrderRepo
"""

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")

customer = Customer(0, "Luca", "Str. Blaga")
customer_repo.save([customer])

dishes = [CookedDish(0, "Pizza", 450, 12, 25), CookedDish(1, "Paste", 350, 24, 45)]
dish_repo.save(dishes)
drinks = drinks_repo.load()

order = Order(0, customer.id, [dishes[0].id, dishes[1].id], [drinks[0].id], time_stamp="8:29")


def order_bill_test():
    bill = order.generate_bill(dishes, drinks)
    order.show_bill(dishes, drinks)
    assert "Pizza" in bill and "Paste" in bill and "156" in bill and "Sprite" in bill


def save_load_order_test():
    order_repo = OrderRepo("orders.txt")
    order_repo.save([order])

    read_order = order_repo.load()[0]
    print(read_order)

    assert read_order == order

def save_order_test():
    order_repo = OrderRepo("orders.txt")
    order_repo.save([order])

    contents = order_repo.read_file().strip()

    s = "0,0,[0;1],[0],156,8:29"

    assert contents == s

def test_order_wait_time():
    order_wait_time = order.generate_estimated_wait_time(dishes)
    print(order_wait_time)

    preparation_time = dishes[0].preparation_time + dishes[1].preparation_time

    preparation_time = f"{preparation_time // 60} : {preparation_time % 60}"

    assert order_wait_time == preparation_time

order_bill_test()
save_order_test()
test_order_wait_time()
save_order_test()