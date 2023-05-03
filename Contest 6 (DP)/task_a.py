def min_cost(cost_mass):
    n = len(cost_mass)
    if n == 1:
        return cost_mass[0]
    dp = [0]*n
    dp[0], dp[1] = cost_mass[0], cost_mass[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost_mass[i]
    return dp[n - 1]


if __name__ == "__main__":
    n = int(input())
    cost_mass = list(map(int, input().split()))
    print(min_cost(cost_mass))