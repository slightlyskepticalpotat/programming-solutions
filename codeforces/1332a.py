import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    if x1 <= x - a + b <= x2 and y1 <= y - c + d <= y2 and (x1 != x2 or max(a, b) == 0) and (y1 != y2 or max(c, d) == 0): # sometimes nowhere to move
        print("YES")
    else:
        print("NO")