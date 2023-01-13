from functools import reduce

from L5v2.models.Order import Order
from L5v2.repository.DataRepo import DataRepo

class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, obj_list):
        """
        :param obj_list: a list of type order
        :return: the list as a string
        """
        string_list = map(lambda item: f"{item.id},{item.customer_id},{list_to_string(item.dish_ids)},{list_to_string(item.drinks_ids)},{item.costs},{item.time_stamp}",obj_list)
        return reduce(lambda s1, s2: s1 + '\n' + s2, string_list)

    def convert_from_string(self, string):
        """
        :param string: list of orders as a string
        :return: string as a list
        """
        if string == "":
            return []

        def line_to_dash(line):
            """
            :param line: a line from file
            :return: list of string split after ,
            """

            params: list[str] = line.split(',')
            dish_string = params[2].strip("[]")
            dishes = [] if dish_string == "" else list(map(lambda dish: int(dish), dish_string.split(';')))

            drink_string = params[3].strip("[]")
            drinks = [] if drink_string == "" else list(map(lambda dish: int(dish), drink_string.split(';')))

            return Order(int(params[0]), int(params[1]), dishes, drinks, int(params[4]), params[5])

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))

def list_to_string(lst):
    """
    lst : a list of ids
    :return:
    """
    string = "["
    for el in lst:
        string += str(el) + ';'
    string = string[:-1]
    return string + ']'