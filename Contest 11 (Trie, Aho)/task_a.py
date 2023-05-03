def pref_func(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while True:
            if s[i] == s[k]:
                pi[i] = k + 1
                break
            if k == 0:
                break
            k = pi[k - 1]
    return pi


if __name__ == '__main__':
    s_1 = input()
    s_2 = input()
    pi = pref_func(s_2 + "#" + s_1)
    ans = []
    n = len(s_2)
    m = len(s_1)
    for i in range(n + 1, m + n + 1):
        if pi[i] == n:
            ans.append(i - 2*n)
    print(*ans)


