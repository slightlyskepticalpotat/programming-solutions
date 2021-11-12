import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    if len([i for i in vals if i % 2]) == n:
        print("Yes")
    else:
        print("No")