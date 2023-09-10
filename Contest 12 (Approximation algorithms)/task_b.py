from math import exp
from random import random, randint


def change(t):
    theta_new = t.copy()
    a, b = randint(0, len(t) - 1), randint(0, len(t) - 1)
    if a > b:
        theta_new[b:a+1] = t[b:a+1][::-1]
    else:
        theta_new[a:b+1] = t[a:b+1][::-1]
    return theta_new


def f(t, values):
    dist = 0
    for i in range(len(t)-1):
        dist += values[t[i]][t[i + 1]]
    return dist


def otzig_method(values: list[list[int]]):
    T = 100
    theta = [i for i in range(len(values))]
    curr_f = f(theta, values)
    i = 0
    while i < 10**5:
        if curr_f == 0:
            break
        theta_new = change(theta)
        f_new = f(theta_new, values)
        if f_new - curr_f <= 0 or exp((curr_f - f_new) / T) > random():
            theta = theta_new
            curr_f = f_new
            print(curr_f)
        T *= 0.99
        i += 1
    return theta, curr_f


if __name__ == '__main__':
    arr = [[0] * 312 for _ in range(312)]
    with open('text.txt', 'r') as file:
        row = 0
        col = 0
        for line in file:
            lst_val = line.rsplit()
            for val in lst_val:
                arr[row][col] = int(val)
                col += 1
                if col == 312:
                    row += 1
                    col = 0
                    if row == 312:
                        break
    ans = otzig_method(arr)
    print('\n' + str(ans[1]))
    for value in ans[0]:
        print(value + 1, end=' ')
