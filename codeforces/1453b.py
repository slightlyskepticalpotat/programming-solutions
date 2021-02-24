import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    total, best = sum([abs(values[i] - values[i - 1]) for i in range(1, n)]), max(abs(values[0] - values[1]), abs(values[-1] - values[-2]))
    for i in range(1, n - 1):
        best = max(best, abs(values[i - 1] - values[i]) + abs(values[i + 1] - values[i]) - abs(values[i + 1] - values[i - 1])) # make equal to higher or lower
    print(total - best)
