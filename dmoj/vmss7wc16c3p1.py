import sys

input = sys.stdin.readline

max_x, max_y, min_x, min_y = 0, 0, float("inf"), float("inf")
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
print((max_x - min_x) * (max_y - min_y))