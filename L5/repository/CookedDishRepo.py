from L5.modelle.CookedDish import CookedDish
from L5.repository.DataRepo import DataRepo

class CookedDishRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, objects):
        result_string = ""
        for object in objects:
            result_string += str(object.id) + ','
            result_string += str(object.preparation_time) + ','
            result_string += str(object.serving_size) + ','
            result_string += str(object.price) + ','
        return result_string

    def convert_from_string(self, string_objects):
        objects = []
        for line in string_objects:
            line = line.strip()
            object_parts = line.split(',')
            cooked_dish = CookedDish(object_parts[1], object_parts[2], object_parts[3])
            objects += [cooked_dish]
        return objects
