import sys

sys.stdin = open("feast.in", "r")
sys.stdout = open("feast.out", "w")

t, a, b = map(int, input().split())
dp = [[0 for i in range(t + 1)] for j in range(2)] # dp[i][j] represents if it's possible to get a fullness of i with or without drinking water
dp[0][0] = 1
for i in range(1, t + 1):
    if i >= a:
        dp[0][i] |= dp[0][i - a]
    if i >= b:
        dp[0][i] |= dp[0][i - b]
    dp[1][i // 2] |= dp[0][i] # we can drink water once
for i in range(1, t + 1):
    if i >= a:
        dp[1][i] |= dp[1][i - a]
    if i >= b:
        dp[1][i] |= dp[1][i - b]
for i in range(t, -1, -1):
    if dp[1][i] or dp[0][i]:
        print(i)
        break
