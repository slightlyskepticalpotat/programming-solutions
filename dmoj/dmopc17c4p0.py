import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(round(min(dist(x1, y1, x2, y2), dist(x1, y1, x3, y3), dist(x2, y2, x3, y3)) ** 2))