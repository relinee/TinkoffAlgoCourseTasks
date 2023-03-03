''' 11 смен
7
38 27 43 3 9 82 10
'''
import sys
count_inversion = 0

def merge_sort(a: list[int]):
    a_len = len(a)
    middle = int(a_len / 2)
    if a_len == 1:
        return a
    return merge_with_a_feathure(merge_sort(a[:middle]), merge_sort(a[middle:]))


def merge_with_a_feathure(a: list[int], b: list[int]):
    ptr_a, ptr_b = 0, 0
    res = []
    global count_inversion
    while ptr_a < len(a) and ptr_b < len(b):
        if a[ptr_a] < b[ptr_b]:
            res += [a[ptr_a]]
            ptr_a += 1
        else:
            res += [b[ptr_b]]
            ptr_b += 1
            count_inversion += 1 * (len(a) - ptr_a)
    #print("1", res,":", a,"+", b, ":", count_inversion)
    while ptr_a < len(a):
        res += [a[ptr_a]]
        ptr_a += 1
    while ptr_b < len(b):
        res += [b[ptr_b]]
        ptr_b += 1
    #print("2", res,":", a,"+", b, ":", count_inversion, "\n")
    #count_inversion = 0
    return res



if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    n = int(input())
    arr = list(map(int, input().split()))
    count_inversion = 0
    sorted_arr = merge_sort(arr)
    print(count_inversion)
    print(*sorted_arr)
