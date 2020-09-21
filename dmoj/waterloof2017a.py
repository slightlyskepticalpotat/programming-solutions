sticks, triangles = [int(i) for i in input().split()], set()
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            a, b, c = sticks[i], sticks[j], sticks[k]
            if a + b > c and a + c > b and b + c > a:
                triangles.add(tuple(sorted([a, b, c])))
print(len(triangles))