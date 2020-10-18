# barycentric coordinates

import sys

input = sys.stdin.readline

def point_in_triangle(x, y):
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    c = 1 - a - b
    if abs(a - 0.5) <= 0.5001 and abs(b - 0.5) <= 0.5001 and abs(c - 0.5) <= 0.5001:  # precision issues
        return True
    return False

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
inside = 0
print(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
for _ in range(int(input())):
    x, y = map(int, input().split())
    if point_in_triangle(x, y):
        inside += 1
print(inside)