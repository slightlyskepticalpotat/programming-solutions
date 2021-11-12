import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, best, loc = int(input()), sorted([int(i) for i in input().split()]), 0, 0
    for i in range(1, n):
        best, loc = best - (vals[i] * i - loc), loc + vals[i] # negative edges from current node to cheaper nodes, taking into account current cost
    print(best + vals[-1]) # positive at beginning