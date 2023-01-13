from models.CookedDish import CookedDish
from models.Customer import Customer
from models.Order import Order
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo

"""
In this folder we test the functionalities of the Order class and the functionalities
of the OrderRepo class
"""

customer_repo = CustomerRepo("customers.txt")
dish_repo = CookedDishRepo("dishes.txt")
drinks_repo = DrinkRepo("drinks.txt")

customer = Customer(0, "Mihai", "Str. Ciorilor")
customer_repo.save([customer])

dishes = [CookedDish(0, "Pizza", 450, 12, 25), CookedDish(1, "Ciorba de burta", 350, 24, 45)]
dish_repo.save(dishes)
drinks = drinks_repo.load()

order = Order(0, customer.id, [dishes[0].id, dishes[1].id], [drinks[0].id], time_stamp="8:29")



# print(order)


def order_bill_test():
    bill = order.generate_bill(dishes, drinks)
    order.show_bill(dishes, drinks)
    assert "Pizza" in bill and "Ciorba de burta" in bill and "156" in bill and "Vodka" in bill


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
    # print(contents)
    # print(order_repo.convert_to_string([order]))

    s = "0,0,[0;1],[0],None,8:29"

    assert contents == s


def test_order_wait_time():
    order_wait_time = order.generate_estimated_wait_time(dishes)
    print(order_wait_time)

    prep_t = dishes[0].prep_time + dishes[1].prep_time

    prep_t = f"{prep_t // 60} : {prep_t % 60}"

    assert order_wait_time == prep_t


# order_bill_test()
# save_load_order_test()
# test_order_wait_time()
save_order_test()