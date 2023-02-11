import math


def find_x(c):
    l = 0.0
    r = c
    while r - l >= 10 ** -6:
        x = (l + r) / 2
        if x ** 2 + math.sqrt(x + 1) <= c:
            l = x
        else:
            r = x
    print( (l+r) / 2)


if __name__ == '__main__':
    c = float(input())
    find_x(c)