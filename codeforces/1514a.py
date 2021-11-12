import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if any(math.sqrt(char) != math.floor(math.sqrt(char)) for char in values):
        print("YES")
    else:
        print("NO")
