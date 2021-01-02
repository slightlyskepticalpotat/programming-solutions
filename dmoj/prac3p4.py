import sys

input = sys.stdin.readline

def change(coins, x):
    dp = [0 for i in range(x + 1)] # smallest number of coins we can use to make i
    for i in range(1, x + 1):
        dp[i] = float("inf")
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1]

while True:
    m, n = map(int, input().split())
    if m + n == 0:
        break
    buckets = [int(input()) for _ in range(n)]
    print(change(buckets, m))