def max_square(n, m, mass_elem):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mass_elem[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    max_size = 0
    ind_max_sq = (0, 0)
    for i in range(n):
        for j in range(m):
            if dp[i][j] > max_size:
                max_size = dp[i][j]
                ind_max_sq = (i - max_size + 2, j - max_size + 2)
    return max_size, ind_max_sq


if __name__ == '__main__':
    n, m = map(int, input().split())
    mass_elem = [[0] * m for _ in range(n)]
    for i in range(n):
        mass_elem[i] = list(map(int, input().split()))
    max_sz, ind_max_sq = max_square(n, m, mass_elem)
    print(max_sz)
    print(*ind_max_sq)
