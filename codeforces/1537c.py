import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), list(sorted([int(i) for i in input().split()]))
    if n != 2: # if n == 2, print in order
        best, best_i = float("inf"), -1
        for i in range(1, n):
            if abs(vals[i] - vals[i - 1]) < best:
                best = abs(vals[i] - vals[i - 1])
                best_i = i
        vals = vals[best_i:] + vals[:best_i]
    print(*vals)
