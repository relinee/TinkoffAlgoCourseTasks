def prefix_polynomial_hash(str, k, mod, pow_mass):
    h = [0] * (len(str) + 1)
    i = 0
    for s in str:
        x = int(ord(s) - ord('a') + 1)
        h[i + 1] = int((h[i] + x * pow_mass[i]) % mod)
        i += 1
    return h


def get_prefix_substr(pref_hash, l, r, pow_mass, mod, n):
    return int((pref_hash[r + 1] - pref_hash[l]) * pow_mass[n-l] % mod)


def get_pow_mass(n, mod, k):
    p = [1] * n
    for i in range(1, n):
        p[i] = int((p[i - 1] * k) % mod)
    return p


if __name__ == '__main__':
    mod = 10**9+7
    k = 31
    s = input()
    n = int(input())
    pow_mass = get_pow_mass(len(s) + 1, mod, k)
    pref_hash_s = prefix_polynomial_hash(s, k, mod, pow_mass)
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        p1 = get_prefix_substr(pref_hash_s, a - 1, b - 1, pow_mass, mod, len(s))
        p2 = get_prefix_substr(pref_hash_s, c - 1, d - 1, pow_mass, mod, len(s))
        if p1 == p2:
            print("Yes")
        else:
            print("No")
