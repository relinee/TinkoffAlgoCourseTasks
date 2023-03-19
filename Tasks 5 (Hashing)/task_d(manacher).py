def manacher_odd(s: str):
    n = len(s)
    d = [1] * n
    left, right = 0, 0
    for i in range(1, n):
        tmp = d[i]
        if i < right:
            tmp = min(right - i + 1, d[left + right - i])
        while i - tmp >= 0 and i + tmp < n and s[i - tmp] == s[i + tmp]:
            tmp += 1
        d[i] = tmp
        if i + tmp - 1 > right:
            left = i - tmp + 1
            right = i + tmp - 1
    return sum(d)


def manacher_even(s: str):
    n = len(s)
    d = [0] * n
    left, right = -1, -1
    for i in range(n - 1):
        tmp = d[i]
        if i < right:
            tmp = min(right - i, d[left + right - i - 1])
        while i - tmp >= 0 and i + tmp + 1 < n and s[i - tmp] == s[i + tmp + 1]:
            tmp += 1
        d[i] = tmp
        if i + tmp > right:
            left = i - tmp + 1
            right = i + tmp
    return sum(d)


# Алгоритм Манакера
if __name__ == '__main__':
    s = input()
    print(manacher_even(s) + manacher_odd(s))
