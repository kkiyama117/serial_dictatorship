class Thing:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name is other.name

    def __str__(self):
        return "things: {}".format(self.name)


class Person:
    def __init__(self, name: str, priority: list):
        self.priority = priority
        self.name = name
        self.thing = None

    def __str__(self):
        return self.name
