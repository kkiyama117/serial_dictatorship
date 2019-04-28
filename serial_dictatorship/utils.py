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
def check_priorities(priorities):
    len_list = [len(priority) for priority in priorities]
    return len(len_list) is len_list.count(len_list[0])
