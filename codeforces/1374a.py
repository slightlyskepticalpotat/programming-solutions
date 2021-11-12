import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y, n = map(int, input().split())
    if ((n // x) * x + y) <= n:
        print((n // x) * x + y)
    else:
        print((n // x) * x + y - x)
