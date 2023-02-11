import sys


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


if __name__ == '__main__':
    n = int(input())
    arr = list(range(1, int(n) + 1))
    l = 0
    r = len(arr) - 1
    last_sign = ""
    while l <= r:
        m = (l + r) // 2
        if query(arr[m]) == "<":
            r = m - 1
        else:
            l = m + 1
    print("!", arr[r])
