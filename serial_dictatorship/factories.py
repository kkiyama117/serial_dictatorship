# 取り敢えず雑に別実装(Factory)にすげ替えられるように実装
import random

from serial_dictatorship.models import Person, Thing
from serial_dictatorship.utils import _is_things_list


# Person, priority, 等の準備
def prepare(priorities: list):
    people = [Person('person{}'.format(count + 1), str_priority) for count, str_priority in
              enumerate(priorities)]
    print("create: ", [person.name for person in people])
    return people


def run(priorities: list):
    # Person, priority, 等の準備
    people = prepare(priorities)

    # step 0
    # peopleをランダムに順番付けする
    random.shuffle(people)
    # step 1
    # 一番前の人が一番好むものを選ぶ

    return people
