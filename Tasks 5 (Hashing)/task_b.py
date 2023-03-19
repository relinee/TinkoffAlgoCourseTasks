def polynomial_hash(str, k, mod):
    h = 0
    for s in str:
        x = int(ord(s) - ord('a') + 1)
        h = (h * k + x) % mod
    return h


def prefix_polynomial_hash(str, k, mod):
    h = [0] * (len(str) + 1)
    i = 0
    for s in str:
        x = int(ord(s) - ord('a') + 1)
        h[i + 1] = (h[i] * k + x) % mod
        i += 1
    return h


# Алгоритм Рабина - Карпа
if __name__ == '__main__':
    mod = 10**9 + 7
    k = 31
    s = input()
    checking_subs = input()
    pref_hash_s = prefix_polynomial_hash(s, k, mod)
    poly_hash_subs = polynomial_hash(checking_subs, k, mod)
    n, m = len(s), len(checking_subs)
    p_m = (k ** m) % mod
    ans = list()
    for i in range(n - m + 1):
        p = (pref_hash_s[i + m] - pref_hash_s[i] * p_m) % mod
        if p == poly_hash_subs:
            ans.append(i)
    print(*ans, end="")
