
def count_itteration_in_sort(n: int, arr_ind: list[int]):
    print(1, end=' ')
    a = [0 for _ in range(n)]
    left_border = -1
    count_itt = 0
    for i in range(n):
        ind_itt = arr_ind[i] - 1
        a[ind_itt] = 1
        if ind_itt == n - 1:
            j = 1
            while a[ind_itt - j] == 1 and ind_itt - j != -1:
                j += 1
            count_itt -= j - 1
            left_border = ind_itt - j + 1
        elif left_border != -1:
            if ind_itt + 1 == left_border:
                j = 1
                while ind_itt - j != -1 and a[ind_itt - j] == 1:
                    j += 1
                count_itt -= j - 1
                left_border = ind_itt - j + 1
            else:
                count_itt += 1
        else:
            count_itt += 1
        print(count_itt + 1, end=' ')


if __name__ == '__main__':
    n = int(input())
    arr_ind = list(map(int, input().split()))
    count_itteration_in_sort(n, arr_ind)
