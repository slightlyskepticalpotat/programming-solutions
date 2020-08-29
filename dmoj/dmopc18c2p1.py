import sys
input = sys.stdin.readline

top, right, bottom, left = -1000000, -1000000, 1000000, 1000000
for i in range(int(input())):
    x, y = map(int, input().split())
    if x > top:
        top = x
    elif x < bottom:
        bottom = x
    if y > right:
        right = y
    elif y < left:
        left = y
print(2 * ((top - bottom) + (right - left)))