def point_in_triangle(x, y, z, point_x, point_y):
    a = ((y[1] - z[1]) * (point_x - z[0]) + (z[0] - y[0]) * (point_y - z[1])) / ((y[1] - z[1]) * (x[0] - z[0]) + (z[0] - y[0]) * (x[1] - z[1]))
    b = ((z[1] - x[1]) * (point_x - z[0]) + (x[0] - z[0]) * (point_y - z[1])) / ((y[1] - z[1]) * (x[0] - z[0]) + (z[0] - y[0]) * (x[1] - z[1]))
    c = 1 - a - b
    if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        return True
    return False

n, m = map(int, input().split())
cities = [tuple(int(i) for i in input().split()) for _ in range(n)]

for _ in range(m):
    hit = 0
    a, b, c, d, e, f = map(int, input().split())
    for city in cities:
        if point_in_triangle((a, b), (c, d), (e, f), city[0], city[1]):
            hit += 1
    print(hit)