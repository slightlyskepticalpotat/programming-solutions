import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()] + [0]
    dp = [[float("inf"), float("inf")] for i in range(n + 1)] # dp[i][j] current pos i, j is player (0 us,  1 friend)
    dp[0][1] = 0
    for i in range(n):
        for j in range(2):
            for k in range(1, min(n - i, 2) + 1):
                new = values[i] + values[i + 1] * (k - 1)
                dp[i + k][(j + 1) % 2] = min(dp[i + k][(j + 1) % 2], dp[i][j] + j * new)
    print(min(dp[n][0], dp[n][1]))
