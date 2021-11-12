import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = a * b
    y = x + a
    z = x + y
    if z % (a * b):
        print("YES")
        print(x, y, z)
    else:
        print("NO")
