def func_value(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def find_x(a, b, c, d):
    l = -10 ** 5
    r = 10 ** 5
    if (a < 0.0):
        l, r = r, l
    while abs(r - l) >= 10 ** -4:
        x = (l + r) / 2
        if func_value(a, b, c, d, x) < 0.0:
            l = x
        else:
            r = x
    print(r)


if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    find_x(a, b, c, d)
