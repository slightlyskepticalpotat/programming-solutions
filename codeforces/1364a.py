import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    vals = [int(i) for i in input().split()]
    if sum(vals) % x:
        print(n)
    elif all(not i % x for i in vals):
        print(-1)
    else:
        for i in range(n):
            if vals[i] % x:
                l = i
                break
        for i in range(n - 1, -1, -1):
            if vals[i] % x:
                r = i
                break
        print(n - min(l + 1, n - r))