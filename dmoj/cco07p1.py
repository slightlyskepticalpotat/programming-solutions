import math, sys

input = sys.stdin.readline

def convex_hull(x): # convex hull with andrew's algorithm
    x.sort(key = lambda x: (x[0], x[1])) # sort by x and y coordinates
    upper_hull, lower_hull = [], []
    for point in reversed(x):
        while len(upper_hull) > 1 and clockwise(upper_hull[-2], upper_hull[-1], point):
            upper_hull.pop()
        upper_hull.append(point)
    for point in x:
        while len(lower_hull) > 1 and clockwise(lower_hull[-2], lower_hull[-1], point):
            lower_hull.pop()
        lower_hull.append(point)
    return upper_hull[:-1] + lower_hull[:-1] # remove duplicate point

def clockwise(x, y, z): # direction of xy and yz
    dot_product = (x[0] - y[0]) * (z[1] - y[1]) - (x[1] - y[1]) * (z[0] - y[0])
    if dot_product <= 0: # clockwise or straight ahead
        return True
    elif dot_product > 0:
        return False

def shoelace(x):
    area = 0
    for i in range(-1, len(x) - 1):
        area += x[i][0] * x[i + 1][1] - x[i][1] * x[i + 1][0]
    return area / 2

points = [tuple(int(i) for i in input().split()) for _ in range(int(input()))]
print(int(shoelace(convex_hull(points)[::-1]) // 50)) # counter-clockwise order for shoelace