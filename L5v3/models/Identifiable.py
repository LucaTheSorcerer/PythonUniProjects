class Identifiable:
    next_ID = 100

    def __init__(self, id_: int = None):
        self.id = id_ if id_ is not None else Identifiable.next_ID
        Identifiable.next_ID += 1
