from functools import reduce

from models.CookedDish import CookedDish
from repository.DataRepo import DataRepo


class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, dishes):
        """
        :param dishes: A list of type CookedDish
        :return: The list as a string
        """
        str_list = list(
            map(lambda item: f"{item.id},{item.name},{item.portion_size},{item.price},{item.prep_time}", dishes))
        return reduce(lambda s1, s2: s1 + '\n' + s2, str_list)

    def convert_from_string(self, string: str):
        """
        :param string: The representation of a list of dishes as a string
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
            return CookedDish(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))
