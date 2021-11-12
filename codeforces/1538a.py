import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    most, least = vals.index(max(vals)), vals.index(min(vals))
    most, least = max(most, least), min(most, least)
    print(min([least + 1 + n - most, n - least, most + 1])) # assume least is further left
