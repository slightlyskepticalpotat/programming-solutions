import sys

input = sys.stdin.readline

n = int(input())
dice, dp, mod = [1, 2, 3, 4, 5, 6], [0 for _ in range(n + 1)], 10 ** 9 + 7 # dp[i] represents the number of ways to add to i
dp[0] = 1
for i in range(1, n + 1):
    for roll in dice:
        if i >= roll:
            dp[i] = (dp[i] + dp[i - roll]) % mod
print(dp[n])
