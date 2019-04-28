# 取り敢えず雑に別実装(Factory)にすげ替えられるように実装
from serial_dictatorship.models import Person, Thing
from serial_dictatorship.utils import _is_things_list


class MainFactory:
    def __init__(self):
        pass

    @classmethod
    def run(cls, priorities: list):
        # Person, priority, 等の準備
        people = [cls.create_person('person{}'.format(count + 1), str_priority) for count, str_priority in
                  enumerate(priorities)]
        print("create: ", [person.name for person in people])
        return people

    @classmethod
    def create_person(cls, name: str, priority: list):
        if _is_things_list(priority):
            return Person(name, priority)
        else:
            priority = [Thing(n) for n in priority]
            return Person(name, priority)
