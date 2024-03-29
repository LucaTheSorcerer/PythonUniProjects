from functools import reduce

from L5v3.models.Drink import Drink
from L5v3.repository.DataRepo import DataRepo


class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, drinks):
        """
        :param drinks: list of type Drinks
        :return: list as a string
        """
        str_list = map(lambda item: f"{item.id},{item.name},{item.portion_size},{item.price},{item.alcohol}", drinks)
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string):
        """
        :param string: list of drinks as a string
        :return: string converted in the form of a list
        """
        if string == "":
            return []

        def line_to_dash(line):
            """
            :param line: A line from the file
            :return: A list of strings split after ','
            """
            params = line.split(',')
            return Drink(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))
