import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [[[-1 for i in range(2)] for j in range(k + 1)] for l in range(n + 1)] # dp[n][k][d] = number of particles there, k is reversed
    for i in range(1, n + 1):
        dp[i][1][0], dp[i][1][1] = 1, 1
    for i in range(2, k + 1):
        for j in range(n, 0, -1):
            loc = 2
            if j < n:
                loc += dp[j + 1][i][0] - 1
            if j > 1:
                loc += dp[j - 1][i - 1][1] - 1
            dp[j][i][0] = loc % (10 ** 9 + 7)
        for j in range(1, n + 1):
            loc = 2
            if j < n:
                loc += dp[j + 1][i - 1][0] - 1
            if j > 1:
                loc += dp[j - 1][i][1] - 1
            dp[j][i][1] = loc % (10 ** 9 + 7)
    print(dp[1][k][0])
