import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(2 ** int(math.log(int(input()), 2)) - 1) # 2 ** msb - 1
