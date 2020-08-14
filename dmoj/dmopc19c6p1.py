import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a1, b1 = y1 - y2, x2 - x1
c1 = -(a1 * x1 + b1 * y1)
a2, b2 = y3 - y4, x4 - x3
c2 = -(a2 * x3 + b2 * y3)
if a1 * b2 == a2 * b1: # slope
    if b1 * c2 == b2 * c1: # intercept
        print("coincident") 
    else:
        print("parallel")
else: # intersection
    print((b1 * c2 - b2 * c1) / (b2 * a1 - b1 * a2), (a1 * c2 - a2 * c1) / (a2 * b1 - a1 * b2))