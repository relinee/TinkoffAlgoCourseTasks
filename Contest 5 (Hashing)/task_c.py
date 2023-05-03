import sys
def prefix_polynomial_hash(str, k, mod):
    h = [0] * (len(str) + 1)
    p = [1] * (len(str) + 1)
    i = 0
    for s in str:
        x = int(ord(s) - ord('a') + 1)
        h[i + 1] = (h[i] * k + x) % mod
        i += 1
        p[i] = (p[i - 1] * k) % mod
    return h, p


def get_prefix_substr_hash(pref_hash, l, r, pow_mass, mod):
    return (pref_hash[r + 1] - pref_hash[l] * pow_mass[r - l + 1] % mod + mod) % mod


def is_equal(m, pref_hash_s, pref_hash_subs, pow_mass, mod, a):
    for j in range(m - 1):
        p1 = get_prefix_substr_hash(pref_hash_s, a, a + j, pow_mass, mod)
        p2 = get_prefix_substr_hash(pref_hash_subs, 0, j, pow_mass, mod)
        if p1 != p2:
            p1 = get_prefix_substr_hash(pref_hash_s, a + j + 1, a + m - 1, pow_mass, mod)
            p2 = get_prefix_substr_hash(pref_hash_subs, j + 1, m - 1, pow_mass, mod)
            if p1 == p2:
                return True
            else:
                return False
    return True

if __name__ == '__main__':
    mod = 10 ** 9 + 9
    k = 35
    checking_subs = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    n, m = len(s), len(checking_subs)
    pref_hash_s, pow_mass = prefix_polynomial_hash(s, k, mod)
    pref_hash_subs, _ = prefix_polynomial_hash(checking_subs, k, mod)
    ans = list()
    if m > n:
        print(0)
    else:
        for i in range(n - m + 1):
            a = i
            b = i + m
            p1 = get_prefix_substr_hash(pref_hash_s, a, b - 1, pow_mass, mod)
            p2 = get_prefix_substr_hash(pref_hash_subs, 0, m - 1, pow_mass, mod)
            if p1 == p2:
                ans.append(i + 1)
            else:
                if is_equal(m, pref_hash_s, pref_hash_subs, pow_mass, mod, a):
                    ans.append(i + 1)
        print(len(ans))
        print(*ans, end="")