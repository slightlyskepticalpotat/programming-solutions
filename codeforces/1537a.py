import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    total, length = sum(vals), len(vals)
    if total < length:
        print(1)
    elif total == length:
        print(0)
    else:
        print(total - length)
