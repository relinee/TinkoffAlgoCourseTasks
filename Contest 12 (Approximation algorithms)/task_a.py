from math import exp
from random import random, randint


def change(t):
    theta_new = t.copy()
    a, b = randint(0, len(t) - 1), randint(0, len(t) - 1)
    theta_new[a], theta_new[b] = theta_new[b], theta_new[a]
    return theta_new


def f(t):
    n = len(t)
    mist = 0
    for i in range(n):
        for j in range(i + 1, n):
            # если один валит другого
            if t[i] == t[j] or t[i] - t[j] == i - j or t[i] - t[j] == j - i:
                mist += 1
    return mist


def otzig_method(n):
    T = 100
    theta = [i for i in range(n)]
    while True:
        curr_f = f(theta)
        if curr_f == 0:
            break
        theta_new = change(theta)
        f_new = f(theta_new)
        if f_new - curr_f <= 0 or exp((curr_f - f_new) / T) > random():
            theta = theta_new
        T *= 0.99
    return theta


if __name__ == '__main__':
    n = int(input())
    ans = otzig_method(n)
    for i in range(n - 1):
        print(ans[i] + 1, end=' ')
    print(ans[n - 1] + 1)