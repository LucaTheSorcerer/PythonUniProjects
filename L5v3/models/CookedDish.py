from models.Dish import Dish


class CookedDish(Dish):
    def __init__(self, id_: int = None, name: str = None, portion_size: int = None, price: int = None,
                 prep_time: int = None):
        super().__init__(id_, name, portion_size, price)
        self.prep_time = prep_time

    def __eq__(self, other):
        return super().__eq__(other) and self.prep_time == other.prep_time

    def __str__(self):
        return super().__str__() + f", preparation Time: {self.prep_time}"
