import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), list(sorted([int(i) for i in input().split()]))
    x = math.factorial(n)
    if vals[-1] != vals[-2]:
        print(int(x - x // (vals.count(vals[-1] - 1) + 1)) % 998244353)
    else:
        print(int(x) % 998244353)
