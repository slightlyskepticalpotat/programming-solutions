import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    r, b, d = map(int, input().split())
    if r == b:
        print("YES")
    elif r > b:
        if math.ceil((r - b) / b) > d:
            print("NO")
        else:
            print("YES")
    elif b > r:
        if math.ceil((b - r) / r) > d:
            print("NO")
        else:
            print("YES")
