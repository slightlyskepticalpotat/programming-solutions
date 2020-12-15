import sys

input = sys.stdin.readline

def lis(x):
    dp = [1] * len(x)
    for i in range(1, len(x)):
        for j in range(0, i):
            if x[i] > x[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
    return max(dp)

sequence = [char for char in input()]
print(26 - lis(sequence))