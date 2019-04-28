# 取り敢えず雑に別実装(Factory)にすげ替えられるように実装
import random

from serial_dictatorship.models import Person, Thing
from serial_dictatorship.utils import format_priorities, check_priorities


# Person, priority, 等の準備
def prepare(priorities: list):
    # create things
    if not check_priorities(priorities):
        raise ValueError("please give priorities having same length")
    else:
        _priorities = format_priorities(priorities)
        # 今回は取り敢えず一文字ずつで対象を作る
        things = [Thing(name) for name in sorted(_priorities[0])]
        print("create: ", ["things:{}".format(thing.name) for thing in things])
    # person with priority
    people = [Person('person{}'.format(count + 1), str_priority) for count, str_priority in
              enumerate(_priorities)]
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
