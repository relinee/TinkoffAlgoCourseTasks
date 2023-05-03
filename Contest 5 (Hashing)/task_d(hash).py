
def is_palindrome(pref_hash, suff_hash, pow_mass, l, r, mod):
    f_hash = (pref_hash[r + 1] + mod - (pref_hash[l] * pow_mass[r - l + 1]) % mod) % mod
    b_hash = (suff_hash[l] + mod - (suff_hash[r + 1] * pow_mass[r - l + 1]) % mod) % mod
    return f_hash == b_hash


def pref_poly_hash(s, k, mod):
    fwd_poly_hash = [0] * (len(s) + 1)
    pow_mass = [1] * (len(s) + 1)
    for i in range(len(s)):
        x = ord(s[i]) - ord('a') + 1
        fwd_poly_hash[i + 1] = ((fwd_poly_hash[i] * k) % mod + x) % mod
        pow_mass[i + 1] = (pow_mass[i] * k) % mod
    return fwd_poly_hash, pow_mass


def suff_poly_hash(s, k, mod):
    bwd_poly_hash = [0] * (len(s) + 1)
    pow_mass = [1] * (len(s) + 1)
    for i in range(len(s) - 1, -1, -1):
        x = ord(s[i]) - ord('a') + 1
        bwd_poly_hash[i] = ((bwd_poly_hash[i + 1] * k) % mod + x) % mod
        pow_mass[len(s) - i] = (pow_mass[len(s) - i - 1] * k) % mod
    return bwd_poly_hash, pow_mass


def palindrome_odd(s, pref_hash, suff_hash, pow_mass, mod):
    n = len(s)
    ans = [0] * n
    for i in range(n):
        l, r = 1, min(i + 1, n - i)
        while l <= r:
            mid = (l + r) // 2
            if is_palindrome(pref_hash, suff_hash, pow_mass, i - mid + 1, i + mid - 1, mod):
                ans[i] = mid
                l = mid + 1
            else:
                r = mid - 1
    return ans


def palindrome_even(s, pref_hash, suff_hash, pow_mass, mod):
    n = len(s)
    ans = [0]*n
    for i in range(n):
        l, r = 1, min(i, n - i)
        while l <= r:
            mid = (l + r) // 2
            if is_palindrome(pref_hash, suff_hash, pow_mass, i - mid, i + mid - 1, mod):
                ans[i] = mid
                l = mid + 1
            else:
                r = mid - 1
    return ans


def count_palindrome2(s: str):
    k, mod = 31, 10 ** 9 + 7
    pref_hash, pow_mass = pref_poly_hash(s, k, mod)
    suff_hash, _ = suff_poly_hash(s, k, mod)
    ans = 0
    ans += sum(palindrome_odd(s, pref_hash, suff_hash, pow_mass, mod))
    ans += sum(palindrome_even(s, pref_hash, suff_hash, pow_mass, mod))
    return ans


if __name__ == '__main__':
    str = input()
    print(count_palindrome2(str))
