from L5.modelle.Order import Order
from L5.repository.DataRepo import DataRepo
from functools import reduce
import pickle

class OrderRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, objects):
        result_string = ""
        # for object in objects:
        #     result_string += str(object.customer_id) + ','
        #     result_string += str(object.list_of_meals) + ','
        #     result_string += str(object.list_of_drinks) + ','
        #     result_string += str(object.total_price) + ','

        # result_string = reduce(lambda a, b: a + b, map(lambda object: f"{object.customer_id},{object.list_of_meals},{object.list_of_drinks},{object.total_price}", objects))

        # return result_string
        return pickle.dumps(objects)
    def convert_from_string(self, string_objects):
        # objects = []
        # for line in string_objects:
        #     line = line.strip()
        #     object_parts = line.split(',')
        #     order = Order(object_parts[1], object_parts[2], object_parts[3])
        #     objects += [order]
        # return objects
        return [] if len(string_objects) == 0 else pickle.loads(string_objects)