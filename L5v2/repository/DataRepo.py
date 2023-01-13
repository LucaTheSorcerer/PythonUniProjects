class DataRepo:

    def __init__(self, file):
        self.file = file

    def add(self, obj):
        """
        :param obj: an object to be added
        :return: adds a new item to the database
        """

        obj_list = self.load()
        obj_list.append(obj)
        self.save(obj_list)

    def save(self, obj_list):
        """
        :param obj_list: list of objects to be saved in the repo
        :return: saves the list of objects in the repo
        """
        self.write_to_file(self.convert_to_string(obj_list))

    def load(self):
        """
        :return: returns all items from a specific repo
        """
        return self.convert_from_string(self.read_file())

    def read_file(self):
        """
        :return: the whole content of a repo
        """
        with open(self.file, 'r') as f:
            content = f.read()
            f.close()
        return content

    def write_to_file(self, content):
        """
        :param content: the content to be written in the file
        :return: writes the content to the file
        """
        with open(self.file, 'w') as f:
            f.write(content)
            f.close()

    def convert_to_string(self, obj_list):
        """
        only defined here
        """
        pass

    def convert_from_string(self, string):
        """
        only defined here
        """
        pass