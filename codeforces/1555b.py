import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    W, H = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w, h = map(int, input().split())
    ans = []
    if w + (x2 - x1) <= W:
        if w <= x1 or x2 + w <= W:
            ans.append(0)
        else:
            ans.append(min(w - x1, x2 + w - W))
    if h + (y2 - y1) <= H:
        if h <= y1 or y2 + h <= H:
            ans.append(0)
        else:
            ans.append(min(h - y1, y2 + h - H))
    if ans:
        print(min(ans))
    else:
        print(-1)