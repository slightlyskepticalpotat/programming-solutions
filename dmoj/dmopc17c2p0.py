import math

def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
    
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
xs, ys = map(int, input().split())
d = int(input())
if d >= min(dist(x1, y1, xs, ys), dist(x2, y2, xs, ys)):
    print("Yes")
else:
    print("No")