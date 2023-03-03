def difficult_case(n: int):
    if n == 1:
        return [1]
    if n == 2:
        return [2, 1]
    res = [i+1 for i in range(n)]
    for i in range(2, n):
        res[i], res[i // 2] = res[i // 2], res[i]
    return res


if __name__ == '__main__':
    n = int(input())
    print(*difficult_case(n))
