def count_fibb_works(n, curr_ind_fib):
    if n == 1:
        return 1
    if curr_ind_fib >= len(fibb):
        return 0
    if n < fibb[curr_ind_fib]:
        return 0
    res = count_fibb_works(n, curr_ind_fib + 1)
    if n % fibb[curr_ind_fib] == 0:
        res += count_fibb_works(n // fibb[curr_ind_fib], curr_ind_fib)
    return res


# попробовать записать значения fib в set
# проверять только до половины числа, потом проверить есть ли оно в set - если нет 0, иначе +1
if __name__ == "__main__":
    t = int(input())
    fibb = [2, 3]
    i = 1
    while fibb[i] < 10 ** 18 + 1:
        fibb.append(fibb[i] + fibb[i - 1])
        i += 1
    arr_elem = []
    for _ in range(t):
        elem = int(input())
        arr_elem.append(elem)
    for elem in arr_elem:
        print(count_fibb_works(elem, 0))
