import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    coins = [[int(i) for i in input().split()] for j in range(2)]
    row1, row2, ans = sum(coins[0]), 0, float("inf")
    for i in range(m):
        row1 -= coins[0][i]
        if i != 0:
            row2 += coins[1][i - 1]
        ans = min(ans, max(row1, row2))
    print(ans)