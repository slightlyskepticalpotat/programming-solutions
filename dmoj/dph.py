import sys

input = sys.stdin.readline

h, w = map(int, input().split())
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
plan = [input().strip() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if plan[i][j] != "#" and i + j != 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
print(dp[-1][-1])