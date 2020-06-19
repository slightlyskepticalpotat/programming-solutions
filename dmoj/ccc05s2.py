import sys
input = sys.stdin.readline

x, y = 0, 0
x_bound, y_bound = map(int, input().split())
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if 0 <= x + a <= x_bound:
        x += a
    elif x + a <= 0:
        x = 0
    elif x + a >= x_bound:
        x = x_bound
    if 0 <= y + b <= y_bound:
        y += b
    elif y + b <= 0:
        y = 0
    elif y + b >= y_bound:
        y = y_bound
    print(x, y)