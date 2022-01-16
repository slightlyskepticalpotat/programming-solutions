import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array, dp, MOD = [int(i) for i in input().split()], [[0 for i in range(m + 1)] for j in range(n)], 10 ** 9 + 7 # dp[i][j] is the number of ways to create an (i + 1)-element array with the last element being j

if not array[0]: # we can start with any
    for i in range(1, m + 1):
        dp[0][i] = 1
else:
    dp[0][array[0]] = 1
for i in range(1, n):
    if not array[i]:
        for j in range(1, m + 1):
            dp[i][j] += dp[i - 1][j]
            if j != 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j != m:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    else:
        dp[i][array[i]] += dp[i - 1][array[i]]
        if array[i] != 1:
            dp[i][array[i]] += dp[i - 1][array[i] - 1]
        if array[i] != m:
            dp[i][array[i]] += dp[i - 1][array[i] + 1]
        dp[i][array[i]] %= MOD
print(sum([dp[-1][i] for i in range(1, m + 1)]) % MOD)
