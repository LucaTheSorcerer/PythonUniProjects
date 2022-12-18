from L5.modelle.Customer import Customer
from L5.repository.DataRepo import DataRepo

class CustomerRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def convert_to_string(self, string_objects):
        pass

    def convert_from_string(self, string_objects):
        pass