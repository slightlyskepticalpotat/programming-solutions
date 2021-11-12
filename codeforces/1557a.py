import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    one = max(vals)
    vals.remove(one)
    print(one + sum(vals) / len(vals))