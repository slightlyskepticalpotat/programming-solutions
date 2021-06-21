import statistics, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    k = statistics.mean(vals)
    if k != k // 1:
        print(-1)
    else:
        print(len([i for i in vals if i > k]))
