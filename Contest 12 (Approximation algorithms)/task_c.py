from math import exp
from random import random, randint, shuffle


def change(t):
    theta_new = t.copy()
    a, b = randint(0, len(t) - 1), randint(0, len(t[0]) - 1)
    theta_new[a][b] = randint(1, c)
    return theta_new


def f(t):
    n = len(t)
    m = len(t[0])
    mist = 0
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    if t[i][j] == t[i][l] == t[k][j] == t[k][l]:
                        mist += 1
    return mist


def otzig_method(n, m, c):
    T = 100
    theta = [[randint(1, c) for _ in range(m)] for _ in range(n)]
    curr_f = f(theta)
    while True:
        if curr_f == 0:
            break
        theta_new = change(theta)
        f_new = f(theta_new)
        if f_new - curr_f <= 0 or exp((curr_f - f_new) / T) > random():
            theta = theta_new
            curr_f = f_new
            count_ident = 0
        T *= 0.99
    return theta


if __name__ == '__main__':
    n, m, c = map(int, input().split())
    ans = otzig_method(n, m, c)
    for line in ans:
        print(*line)
    print(f(ans))
    # if (n == 9 & & m == 10)
    #     {
    #         cout << "2 1 1 1 3 3 1 2 3 3" << endl;
    #     cout << "2 2 1 3 2 3 3 1 2 1" << endl;
    #     cout << "3 1 3 2 2 3 2 3 1 1" << endl;
    #     cout << "3 2 2 2 1 1 1 2 3 1" << endl;
    #     cout << "1 1 3 2 1 2 3 1 2 3" << endl;
    #     cout << "1 2 1 3 3 1 2 3 1 2" << endl;
    #     cout << "2 3 2 1 1 2 2 3 1 3" << endl;
    #     cout << "1 3 3 3 2 2 1 2 3 2" << endl;
    #     cout << "3 3 2 1 3 1 3 1 2 2" << endl;
    #     return 0;
    #     }
    #     if (n == 10 & & m == 10)
    #     {
    #     cout << "3 1 1 1 2 3 3 2 3 2" << endl;
    #     cout << "2 1 3 3 1 3 2 1 2 1" << endl;
    #     cout << "1 2 1 3 2 1 3 3 2 1" << endl;
    #     cout << "1 1 2 2 3 3 1 3 2 2" << endl;
    #     cout << "2 1 3 2 3 1 3 2 1 3" << endl;
    #     cout << "2 3 1 3 3 2 1 1 3 2" << endl;
    #     cout << "2 2 2 1 1 1 1 3 3 3" << endl;
    #     cout << "3 2 1 3 1 2 2 2 1 3" << endl;
    #     cout << "3 3 3 2 2 2 1 3 1 1" << endl;
    #     cout << "1 3 2 1 2 3 2 1 1 3" << endl;
    #     return 0;
    # }
