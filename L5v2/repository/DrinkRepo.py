from functools import reduce

from L5v2.models.Drink import Drink
from L5v2.repository.DataRepo import DataRepo

class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, drinks):
        """
        :param drinks: a list of type Drinks
        :return: the list as a string
        """
        string_list = map(lambda item: f"{item.id},{item.name},{item.portion_size},{item.price},{item.alcohol_content}", drinks)
        return reduce(lambda s1, s2: s1 + '\n' + s2, string_list)

    def convert_from_string(self, string):
        """
        :param string: list of drinks as a string
        :return: the string as a list
        """

        if string == "":
            return []

        def line_to_dash(line):
            """
            :param line: a line from the file
            :return: a list of string separated by ,
            """
            params = line.split(',')
            return Drink(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))
