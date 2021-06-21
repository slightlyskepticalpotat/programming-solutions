import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    pivot = values.index(min(values))
    print(n - 1)
    for i in range(n):
        if i != pivot:
            print(i + 1, pivot + 1, values[pivot] + abs(pivot - i), values[pivot])
