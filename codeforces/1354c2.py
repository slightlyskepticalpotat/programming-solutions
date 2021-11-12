import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) * 2
    print(math.cos(math.pi / (2 * n)) / math.sin(math.pi / n))