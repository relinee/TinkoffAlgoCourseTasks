'''5 5
1 3 5 7 9
2 4 8 1 6'''
'''2 2
9 10
9 10
'''
'''
3 3
9 10 11
9 10 11
'''
'''
2 5
0 1
2 4 8 1 6
'''


def search_min_diff(arr, x):
    l = -1
    r = len(arr)
    if r == 1:
        print(arr[r - 1])
        return
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] >= x:
            r = m
        else:
            l = m
    if l == -1:
        l += 1
    if r == len(arr):
        r -= 1
    if abs(arr[l] - x) <= abs(arr[r] - x):
        print(arr[l])
    else:
        print(arr[r])


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_elem = list(map(int, input().split()))
    for i in range(k):
        search_min_diff(arr, arr_elem[i])
