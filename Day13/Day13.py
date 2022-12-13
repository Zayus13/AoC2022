from itertools import zip_longest
from functools import cmp_to_key


def compare(l, r):
    for item in zip_longest(l, r):

        if isinstance(item[0], int) and isinstance(item[1], int):
            if item[0] < item[1]:
                return True
            elif item[0] > item[1]:
                return False
            else:
                continue
        if item[0] is None or item[1] is None:
            return item[0] is None
        if not isinstance(item[1], list):
            item = (item[0], [item[1]])
        if not isinstance(item[0], list):
            item = ([item[0]], item[1])

        res = compare(item[0], item[1])
        if res is None:
            continue
        else:
            return res


def compare_i(l, r):
    if compare(l, r):
        return -1
    else:
        return 1


if __name__ == "__main__":
    input = open("day13.txt", "r").read().split("\n\n")
    i = 1
    res = 0
    ls = [[[2]], [[6]]]
    for packet in input:
        l = eval(packet.splitlines()[0])
        r = eval(packet.splitlines()[1])
        ls.append(l)
        ls.append(r)
        if compare(l, r):
            res += i
        i += 1

    ls = sorted(ls, key=cmp_to_key(compare_i))
    print(res, (ls.index([[2]]) + 1) * (ls.index([[6]]) + 1))
