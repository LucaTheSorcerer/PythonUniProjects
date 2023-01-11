import unittest
from L5.modelle.Customer import Customer
from L5.repository.CustomerRepo import CustomerRepo

customer_repo = CustomerRepo("customers.txt")
customer_repo.clear_database()

customer1 = Customer("Luca", "Str. Blabla1")
customer2 = Customer("Tudor", "Str. Cracra1")
customer3 = Customer("Ion", "Str. Mamata")

customer_repo.add_list([customer1, customer2, customer3])

def test_search_customer_by_name(repo):
    c1 = repo.search(Customer(name="lu"))[0]
    c2 = repo.search(Customer(name="udo"))[0]
    c3 = repo.search(Customer(name="on"))[0]

    assert c1 == customer1 and c2 == customer2 and c3 == customer3

def test_search_customer_by_address(repo):
    c1 = repo.search(Customer(name="lab"))[0]
    c2 = repo.search(Customer(name="acra1"))[0]
    c3 = repo.search(Customer(name="mat"))[0]

    assert c1 == customer1 and c2 == customer2 and c3 == customer3


def test_update_customer(repo, cus):
    customer_id = repo.search(Customer(name="Luca"))[0].id
    repo.update(cus, Customer(name="Andrei"))
    customer = repo.find_by_id(customer_id) #Implement find_by_id

    assert customer.id == customer_id

test_search_customer_by_name(customer_repo)
test_search_customer_by_address(customer_repo)
test_update_customer(customer_repo, customer1)