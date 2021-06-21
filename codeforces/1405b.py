import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, best = int(input()), [int(i) for i in input().split()], 0 # max suffix sum
    for i in range(n):
        best = max(0, best + values[i])
    print(best)
