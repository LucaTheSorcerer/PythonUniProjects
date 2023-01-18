class NotFound(Exception):
    pass


class TodoList:
    def __init__(self, name):
        self.name = name
        self.todos = []

    def done(self, s: str):
        if s not in self.todos:
            raise NotFound
        else:
            index = self.todos.index(s)
            self.todos.remove(s)
            return index


t = TodoList("Mihai")
t.todos.append("Mate")
# print(t.todos)
t.done("Mate")
# print(t.todos)

try:
    t.done("Algebra")
except NotFound:
    # print("It works")
    pass


class ExtraTodoList(TodoList):
    def __init__(self, name):
        super().__init__(name)
        self.done_count = 0

    def done(self, s: str):
        try:
            super().done(s)
            self.done_count += 1
        except NotFound:
            self.done_count -= 1

    def __add__(self, other):
        to = ExtraTodoList(self.name)
        to.todos = self.todos + other.todos
        to.done_count = self.done_count + other.done_count

        return to


e = ExtraTodoList("marcel")
e.todos.append("Algebra")
e.todos.append("Analysis")
print(e.todos)

e.done("Algebra")
e.done("Analysis")

print(e.done_count)

e.done("Sport")
print(e.done_count)

e.todos.append("Advanced Sport")

e2 = ExtraTodoList("Mihai")
e2.todos.append("Sport")
e2.todos.append("Sport2")

e2.done("Sport2")

print(e.todos)
print(e2.todos)

e3 = e + e2

print(e3.name)
print(e3.todos)
print(e3.done_count)