import sys

input = sys.stdin.readline

n, MOD = int(input()), 10 ** 9 + 7
grid, dp = [[i for i in input().strip()] for j in range(n)], [[0 for i in range(n)] for j in range(n)] # dp[i][j] represents number of paths from top left to cell
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == "*":
            dp[i][j] = 0
        elif i + j != 0: # don't recalculate dp[0][0]
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
print(dp[-1][-1])
