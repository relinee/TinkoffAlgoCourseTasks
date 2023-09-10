def min_cost(costs):
    n = len(costs)
    if n == 1:
        return costs[0]
    dp = [0]*n
    dp[0], dp[1] = costs[0], costs[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + costs[i]
    return dp[n - 1]


if __name__ == "__main__":
    n = int(input())
    cost_mass = list(map(int, input().split()))
    print(min_cost(cost_mass))