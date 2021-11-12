import sys

input = sys.stdin.readline

n, m = map(int, input().split())
plan, new = [[int(i) for i in input().split()] for _ in range(n)], [[0 for i in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i + j) % 2:
            new[i][j] = 720720 # lcm 1 to 16
        else:
            new[i][j] = 720720 + plan[i][j] ** 4 # 16 ** 4 = 65536 so in range
for i in range(n):
    print(*new[i])
