import sys

input = sys.stdin.buffer.readline

n, m = input().strip(), input().strip()
dp = [[0] * (len(m) + 1) for j in range(len(n) + 1)] # dp[i][j] is moves to make n[:i] == m[j:]
for i in range(1, len(m) + 1):
    dp[0][i] = i
for i in range(1, len(n) + 1):
    dp[i][0] = i
for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + int(n[i - 1] != m[j - 1]))
print(dp[-1][-1])
