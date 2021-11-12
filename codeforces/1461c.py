import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    values = [int(i) for i in input().split()]
    experiments = [[float(i) for i in input().split()] for j in range(m)]
    best, prob = float("inf"), 1.0
    for i in range(n):
        if values[i] != i + 1:
            best = i + 1
    for experiment in experiments:
        if experiment[0] >= best:
            prob *= (1 - experiment[1])
    if best == float("inf"):
        print(1)
    else:
        print(1 - prob)
