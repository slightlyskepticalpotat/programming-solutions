import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), sorted([int(i) for i in input().split()])
    ans = max([i + 1 if vals[i] <= i + 1 else 0 for i in range(n)])
    print(ans + 1) # herself