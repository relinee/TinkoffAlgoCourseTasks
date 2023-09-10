from functools import cmp_to_key
from sys import stdin


def compare(x, y):
    if x + y <= y + x:
        return 1
    else:
        return -1


if __name__ == '__main__':
    lines = [line.rstrip() for line in stdin]
    # lines = {"2", "20", "004", "66"}
    # lines = {"77", "778", "9"}
    # lines = ["5556", "55565"]
    # lines = ["213","21322"]
    lines = sorted(lines, key=cmp_to_key(compare))
    print(*lines, sep="")
