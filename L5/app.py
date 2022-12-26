from L5.controller.CustomerController import CustomerController
from L5.repository.CustomerRepo import CustomerRepo
from L5.controller.Console import Console

def run():
    controller = Console()
    controller.main_menu()
    # customerRepo = CustomerRepo('repository/database/customer_repo.csv') # layer 1
    # customerController = CustomerController(customerRepo) # layer 2
    # console = Console(customerController) # top layer
    # console.run() # functia run din UI

if __name__ == '__main__':
    run()