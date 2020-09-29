import math

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
xdist, ydist, zdist = abs(a - x), abs(b - y), abs(c - z)
print(max(xdist, max(ydist, zdist)))
print(math.floor(math.sqrt(xdist ** 2 + ydist ** 2 + zdist ** 2)))
print(xdist + ydist + zdist)