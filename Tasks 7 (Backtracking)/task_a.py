def num_win_player(m, n):
    if m == 1 or n == 1:
        return 1

    dp = [["0"] * n for _ in range(m)]

    for i in range(m):
        dp[i][n - 1] = "+"
    for i in range(n):
        dp[m - 1][i] = "+"

    if n < m:
        for i in range(m - n, m):
            dp[i][i - (m - n)] = "+"
    else:
        for i in range(n - m, n):
            dp[i - (n - m)][i] = "+"

    dp[m - 1][n - 1] = "-"

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            if dp[i][j] != "0":
                continue

            dp[i][j] = "-"

            ind_i = i - 1
            ind_j = j
            while ind_i >= 0:
                dp[ind_i][ind_j] = "+"
                ind_i -= 1

            ind_i = i
            ind_j = j - 1
            while ind_j >= 0:
                dp[ind_i][ind_j] = "+"
                ind_j -= 1

            ind_i = i - 1
            ind_j = j - 1
            while ind_i >= 0 and ind_j >= 0:
                dp[ind_i][ind_j] = "+"
                ind_i -= 1
                ind_j -= 1

            break

    if dp[0][0] == "+":
        return 1
    return 2


# https://foxford.ru/wiki/informatika/dvumernoe-dinamicheskoe-programmirovanie-igry
if __name__ == "__main__":
    m, n = map(int, input().split())
    print(num_win_player(m, n))

