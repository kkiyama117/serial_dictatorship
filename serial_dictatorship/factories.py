# 取り敢えず雑に別実装(Factory)にすげ替えられるように実装
import random

from serial_dictatorship.models import Person, Thing
from serial_dictatorship.utils import format_priorities, check_priorities


# Person, priority, 等の準備
def prepare(priorities: list):
    # create things
    _priorities = []
    if check_priorities(priorities):
        _priorities = format_priorities(priorities)
    # 今回は取り敢えず一文字ずつで対象を作る
    # TODO: 本当は hashable にして set(集合)型にするのが適切
    # 一応上の `check_priorities` で文字列をsetにして確認しているので, これでも今の所は問題ない.
    things = create_things(priorities[0], is_to_sort=True)
    print("create: ", ["things:{}".format(thing.name) for thing in things])
    # person with priority
    people = [Person('person{}'.format(count + 1), create_things(str_priority)) for count, str_priority in
              enumerate(_priorities)]
    print("create: ", [person.name for person in people])
    return people, things


def create_things(priority, is_to_sort=False):
    if is_to_sort:
        priority = sorted(priority)
    return [Thing(name) for name in priority]


def run(priorities: list):
    # Person, priority, 等の準備
    people, things = prepare(priorities)

    # step 0
    # peopleをランダムに順番付けする
    random.shuffle(people)
    # step 1~k
    # 一番前の人から一番好むものを選ぶ
    for person in people:
        # priority 内の上から順に
        for desire in person.priority:
            # 残りにあるかを確認して
            if desire in things:
                # あったら取得して
                person.thing = desire
                # 残りのもののリストから削除
                things.remove(desire)
                break
            else:
                # 無かったらpriority の次の要素、という様に続ける
                pass
        # 終了判定
        if not things:
            # 選べるものが無くなったら終了
            break
    # モノの方が多いと全ての人に対しループが回って終了
    return people
