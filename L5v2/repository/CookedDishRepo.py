from functools import reduce

from L5v2.models.CookedDish import CookedDish
from L5v2.repository.DataRepo import DataRepo

class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, dishes):
        """
        :param dishes: list of type CookedDish
        :return: the list as a string
        """
        string_list = list(map(lambda item: f"{item.id},{item.name},{item.portion_size},{item.price},{item.preparation_time}", dishes))
        return reduce(lambda s1, s2: s1 + '\n' + s2, string_list)

    def convert_from_string(self, string: str):
        """
        :param string: the list of dishes as string
        :return: the string as a list
        """
        if string == "":
            return []

        def line_to_dash(line):
            """
            :param line: a line from the file
            :return: list of string split after ,
            """
            params = line.split(',')
            return CookedDish(int(params[0]), params[1], int(params[2]), int(params[3]), int(params[4]))

        lines = string.split('\n')
        return list(map(lambda line: line_to_dash(line), lines))
