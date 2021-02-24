for _ in range(int(input())):
    n, values = int(input()), list(sorted([int(i) for i in input().split()]))
    dp = [[float("inf") for i in range(2 * n)] for j in range(n + 1)] # min value dp[dishes processed][current time]
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(2 * n - 1):
            if dp[i][j] != float("inf") and i < n:
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + abs((values[i] - 1) - j)) # transition state
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
    print(dp[n][2 * n - 1])
