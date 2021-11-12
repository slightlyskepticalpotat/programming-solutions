import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x, t = map(int, input().split())
    full = max(0, n - t // x) * (t // x)
    part = min(n - 1, t // x - 1) * min(n, t // x) // 2
    print(full + part)
