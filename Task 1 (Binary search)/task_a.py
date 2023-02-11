def binary_search(arr, x):
    l = -1
    r = len(arr)
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] > x:
            r = m
        else:
            l = m
    if arr[l] == x:
        print("YES")
    else:
        print("NO")



if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_elem = list(map(int, input().split()))
    for i in range(k):
        binary_search(arr, arr_elem[i])