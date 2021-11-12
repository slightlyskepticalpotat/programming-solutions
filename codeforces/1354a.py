import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    s, t = b, b
    if c > d:
        least = max(math.ceil((a - s) / (c - d)), 0)
        s += least * (c - d)
        t += least * c
    if s >= a:
        print(t)
    else:
        print(-1)