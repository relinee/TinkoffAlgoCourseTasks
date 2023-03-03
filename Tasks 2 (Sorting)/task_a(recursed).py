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


def merge_with_a_feathure(arr_a: list[int], arr_b: list[int]):
    if arr_a[0] < arr_b[0]:
        if len(arr_a) == 1:
            return arr_a + arr_b
        return [arr_a[0]] + merge_with_a_feathure(arr_a[1:], arr_b)
    else:
        global count_inversion
        count_inversion += len(arr_a)
        if len(arr_b) == 1:
            return arr_b + arr_a
        return [arr_b[0]] + merge_with_a_feathure(arr_a, arr_b[1:])


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    n = int(input())
    arr = list(map(int, input().split()))
    count_inversion = 0
    sorted_arr = merge_sort(arr)
    print(count_inversion)
    print(*sorted_arr)
