from functools import reduce

from models.Customer import Customer
from repository.DataRepo import DataRepo


class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        """
        :param obj_list: A list of type Customer
        :return: The list as a string
        """
        str_list = list(map(lambda item: f"{item.id},{item.name},{item.address}", obj_list))
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):
        """
        :param string: The representation of a list of customers as a string
        :return: The string in the form of a list
        """

        if string == "":
            return []

        def line_to_dash(line):
            """
            :param line: A line from the file
            :return: A list of strings split after ','
            """
            params = line.split(',')
            id_ = 0 if params[0] == '' else int(params[0])
            return Customer(id_, params[1], params[2])

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))

    def search(self, name=None, address=None):
        """
        This function should only be used for testing purposes
        It is deprecated
        """
        customers = self.load()
        result = None
        if name is not None:
            result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))

        if address is not None:
            result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))

        return result

    def update(self, customer, name=None, address=None):
        """
        This function should only be used for testing purposes
        It is deprecated
        """
        customers = self.load()
        index = customers.index(customer)
        if name is not None:
            customer.name = name
        if address is not None:
            customer.address = address
        customers[index] = customer

        self.save(customers)
