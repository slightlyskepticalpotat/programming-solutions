import sys

input = sys.stdin.readline

n, x = map(int, input().split())
coins = [[int(i) for i in input().split()] for _ in range(n)]
best = 0
for i in range(n):
    best = max(best, min(coins[i][0], x) * coins[i][1])
print(best)
