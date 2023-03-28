def dist_damerau_lev(str_1, str_2):
    n, m = len(str_1), len(str_2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + 1
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + 1
    for i in range(1,n+1):
        for j in range(1,m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1, dp[i][j-1] + 1)
            if i > 1 and j > 1 and str_1[i - 1] == str_2[j - 2] and str_1[i - 2] == str_2[j - 1]:
                dp[i][j] = min(dp[i][j],dp[i - 2][j - 2] + 1)
    return dp[n][m]


# https://neerc.ifmo.ru/wiki/index.php?title=Задача_о_расстоянии_Дамерау-Левенштейна
if __name__ == "__main__":
    str_1 = input()
    str_2 = input()
    print(dist_damerau_lev(str_1, str_2))