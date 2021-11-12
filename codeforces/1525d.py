import sys

input = sys.stdin.readline

n, values = int(input()), [int(i) for i in input().split()]
start, end = [0] + [i for i in range(n) if values[i] % 2], [0] + [i for i in range(n) if not values[i] % 2]
dp = [[0] + [float("inf")] * (len(start) - 1) for j in range(len(end))] # dp[i][j] is the minimum time if we consider i positions and pick j

for i in range(1, len(end)):
    for j in range(1, len(start)):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + abs(start[j] - end[i]))
print(dp[-1][-1])
