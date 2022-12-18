class DataRepo:
    def __init__(self, file):
        self.file = file
        self.load()
        self.entities : list = []

    def save(self, objects : list):
        for object in objects:
            if object not in self.entities:
                self.entities.append(object)
                self.write_file(self.convert_to_string(self.entities))

    def get_by_id(self, id):
        for entity in self.entities:
            if entity.id == id:
                return entity

    def load(self):
        self.entities = self.read_file() #content ---> string

    def read_file(self):
        with open(self.file, 'r') as file:
            lines = file.readlines()
        return self.convert_from_string(lines)

    def write_file(self, string_content):
        with open(self.file, 'w') as file:
            file.write(string_content)

    def convert_to_string(self, objects):
        pass

    def convert_from_string(self, string_objects):
        pass