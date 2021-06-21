import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    if vals[0] + vals[1] <= vals[-1]:
        print(1, 2, n)
    else:
        print(-1)
