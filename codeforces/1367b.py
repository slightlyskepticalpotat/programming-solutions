import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], 0
    odds, evens = [i for i in range(n) if vals[i] % 2 and not i % 2], [i for i in range(n) if not vals[i] % 2 and i % 2]
    if len(odds) == len(evens):
        print(len(odds))
    else:
        print(-1)