import functools
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    print(functools.reduce(lambda x, y: x & y, vals))