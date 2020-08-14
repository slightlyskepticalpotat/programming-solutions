try:
    import sys, math
    input = sys.stdin.readline

    def distance(x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

    def circumradius(x, y, z):
        global semi
        semi = (x + y + z) / 2
        return 2 * (x * y * z) / (4 * math.sqrt(semi * (semi - x) * (semi - y) * (semi - z)))

    cookies, distances = [], []
    for i in range(int(input())):
        cookies.append([int(i) for i in input().split()])

    for i in range(len(cookies)):
        for j in range(i + 1, len(cookies)):
            for k in range(j + 1, len(cookies)):
                sides = sorted([distance(cookies[i], cookies[j]), distance(cookies[j], cookies[k]), distance(cookies[k], cookies[i])])
                if sides[0] ** 2 + sides[1] ** 2 < sides[2] ** 2: # obtuse triangle
                    distances.append(sides[2])
                else: # acute triangle
                    distances.append(circumradius(sides[0], sides[1], sides[2]))
    print(round(sorted(distances, reverse=True)[0], 2))
except:
    print(semi) # points all overlap