import sys

input = sys.stdin.readline

n, m, sx, sy = map(int, input().split())
for i in range(n):
    if (i + 1) % 2:
        for j in range(m):
            print((i + sx - 1) % n + 1, (j + sy - 1) % m + 1)
    else:
        for j in range(m - 1, -1, -1):
            print((i + sx - 1) % n + 1, (j + sy - 1) % m + 1)
