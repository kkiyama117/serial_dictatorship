from serial_dictatorship.models import Thing


def format_priorities(priorities):
    return [list(priority) for priority in priorities]


def _is_things_list(priority):
    for thing in priority:
        if type(thing) is not Thing:
            return False
    return True


def create_priority_list(priority: list):
    if _is_things_list(priority):
        return priority
    else:
        return [Thing(name) for name in priority]


# kwargsに渡される文字列の形式から問題ないかチェック
# factories の形式(一文字が一個)に依存しているので,形式が変わると使えない
def check_priorities(priorities):
    pri_set_list = [set(priority) for priority in priorities]
    pri_set = first_pri_set = pri_set_list[0]
    for _pri_set in pri_set_list:
        pri_set = pri_set & _pri_set
    if len(pri_set) is not len(priorities[0]):
        raise ValueError("please give priorities having same length")
    elif len(pri_set) is not len(first_pri_set):
        raise ValueError("please give priorities having same things")
    else:
        return True


# 出力されたlist (Person) を整形
def format_output(output: list):
    return ["{}: get {}".format(person.name, person.thing) for person in output]
