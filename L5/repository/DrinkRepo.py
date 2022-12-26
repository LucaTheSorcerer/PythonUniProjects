from L5.modelle.Drink import Drink
from L5.repository.DataRepo import DataRepo
from functools import reduce
import pickle

class DrinkRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, objects):
        result_string = ""
        # for object in objects:
        #     result_string += str(object.id) + ','
        #     result_string += str(object.name) + ','
        #     result_string += str(object.portion_size) + ','
        #     result_string += str(object.price) + ','
        #     result_string += str(object.alcohol_content) + ','

        # result_string = reduce(lambda a, b: a + b, map(lambda object: f"{object.id},{object.name},{object.portion_size},{object.price},{object.alcohol_content}", objects))
        # return result_string
        return pickle.dumps(objects)

    def convert_from_string(self, string_objects):
        # objects = []
        # for line in string_objects:
        #     line = line.strip()
        #     object_parts = line.split(',')
        #     drink = Drink(object_parts[1], object_parts[2], object_parts[3], object_parts[4])
        #     objects += [drink]
        # return objects
        return [] if len(string_objects) == 0 else pickle.loads(string_objects)