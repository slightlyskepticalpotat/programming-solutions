import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.ceil(abs(a - b)/ 10))
