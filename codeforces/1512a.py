import statistics, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    target = statistics.mode(values)
    for i in range(n):
        if values[i] != target:
            print(i + 1)
