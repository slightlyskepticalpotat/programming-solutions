import sys

input = sys.stdin.readline

def change(coins, x):
    dp = [0 for i in range(x + 1)]
    for i in range(1, x + 1):
        dp[i] = float("inf") # infinite
        for coin in coins: # focus on the first coin used
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1) # can we use fewer coins?
    return dp[-1]

x = int(input())
coins = [int(input()) for _ in range(int(input()))]
print(change(coins, x))