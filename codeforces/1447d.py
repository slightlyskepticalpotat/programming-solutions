import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y = input().strip(), input().strip()
dp, best = [[0] * (m + 1) for _ in range(n + 1)], 0
for i in range(n):
    for j in range(m):
        if x[i] == y[j]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 2) # not 4
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] - 1, dp[i][j - 1] - 1)
        best = max(best, dp[i][j], dp[i - 1][j])
print(best)
