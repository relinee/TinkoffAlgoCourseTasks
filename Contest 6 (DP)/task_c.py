def num_moves(n, m):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    curr_i, curr_j = 0, 0
    while curr_i < n - 1 or curr_j < m - 1:
        if curr_i == n - 1:
            curr_j += 1
        else:
            curr_i += 1
        i, j = curr_i, curr_j
        while j < m and i >= 0:
            if j - 2 >= 0:
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j-2]
                if i + 1 < n:
                    dp[i][j] += dp[i+1][j-2]
            if i - 2 >= 0:
                if j - 1 >= 0:
                    dp[i][j] += dp[i-2][j-1]
                if j + 1 < m:
                    dp[i][j] += dp[i-2][j+1]
            j += 1
            i -= 1
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(num_moves(n, m))
    #print(num_moves(4, 4))  # 2
    #print(num_moves(7, 15))  # 13309