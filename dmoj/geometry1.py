import sys, math
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)

for i in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    p = dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1)
    a = math.sqrt(p/2 * (p/2 - dist(x1, y1, x2, y2)) * (p/2 - dist(x2, y2, x3, y3)) * (p/2 - dist(x3, y3, x1, y1)))
    print(round(a, 2), round(p, 2))