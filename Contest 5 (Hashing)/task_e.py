
def all_substrings_hash(lst, hash, mod):
    n = len(lst)
    substrings_hash = set()
    for i in range(n):
        for j in range(i+1, n+1):
            elem_hash = get_hash_sublst(hash, i, j - 1, mod)
            if elem_hash not in substrings_hash:
                substrings_hash.add((elem_hash, j-i))
    return substrings_hash


def get_list_hash(lst, k, mod):
    h = [0] * (len(lst) + 1)
    i = 0
    for elem in lst:
        # Тут можно поиграться
        x = int(elem) + k
        h[i + 1] = (h[i] + x ** 10 % mod) % mod
        i += 1
    return h


def get_hash_sublst(hash, l, r, mod):
    res = ((hash[r + 1] - hash[l]) % mod + mod) % mod
    return res


def get_max_anagram_subarray_length(a, b, n, m):
    k, mod = 31, 10 ** 9 + 7
    hash_a = get_list_hash(a, k, mod)
    hash_b = get_list_hash(b, k, mod)

    all_subs_a = all_substrings_hash(a, hash_a, mod)
    all_subs_b = all_substrings_hash(b, hash_b, mod)

    max_len = 0
    i = 0
    for elem in all_subs_b:
        if elem in all_subs_a:
            len_elem = elem[1]
            max_len = max(len_elem, max_len)
        i += 1
    return max_len


# Хешировать каждый элемент двух списков и потом доставать как в полиномиальном хешировании.
# Не использовать хеширование через 2^ - не очень оптимально
if __name__ == '__main__':
    # n = "3"
    # a = "1 1 1"
    # m = "5"
    # b = "2 1 3 1 1"
    #6
    #5 1 2 2 3 4
    #3
    #3 2 1
    n = int(input())
    a = input().split()
    m = int(input())
    b = input().split()
    print(get_max_anagram_subarray_length(a, b, n, m))
