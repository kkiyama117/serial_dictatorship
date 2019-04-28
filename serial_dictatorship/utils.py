from serial_dictatorship.models import Thing


# TODO: 関数型プログラミングで(forを回さない事で)数十倍早く出来ますが、そこまでのものを想定してないので簡略に見通しを優先しました.
def format_priorities(priorities):
    result = []
    for priority in priorities:
        a = [n for n in priority]
        result.append(a)
    return result


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
