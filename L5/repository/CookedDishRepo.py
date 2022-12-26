import pickle
from L5.modelle.CookedDish import CookedDish
from L5.repository.DataRepo import DataRepo
from functools import reduce

class CookedDishRepo(DataRepo):
    def __init__(self, file = None):
        super().__init__(file)

    def convert_to_string(self, objects):
        return pickle.dumps(objects)
        result_string = ""
        #
        # for object in objects:
        #     result_string += str(object.id) + ','
        #     result_string += str(object.name) + ','
        #     result_string += str(object.portion_size) + ','
        #     result_string += str(object.price) + ','
        #     result_string += str(object.preparation_time) + ','
        #result_string = reduce(lambda a, b:  a + b,  map(lambda object: f"{object.id},{object.name},{object.portion_size},{object.price},{object.preparation_time}", objects))
        #return result_string


        #return result_string

    def convert_from_string(self, string_objects):
        return [] if len(string_objects) == 0 else pickle.loads(string_objects)
        # objects = []
        # for line in string_objects:
        #     line = line.strip()
        #     object_parts = line.split(',')
        #     cooked_dish = CookedDish(object_parts[1], object_parts[2], object_parts[3])
        #     objects += [cooked_dish]
        # return objects
