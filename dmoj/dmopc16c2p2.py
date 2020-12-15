import sys

input = sys.stdin.readline

def find(x):
    if x == path[x]:
        return x
    path[x] = find(path[x])
    return path[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if size[x] < size[y]:
        x, y = y, x
    size[x] += size[y]
    path[y] = x

n, m = map(int, input().split())
path, size = [i for i in range(n + 1)], [1 for i in range(n + 1)]
for _ in range(m):
    line = [int(i) for i in input().split()][1:]
    for student1 in line:
        for student2 in line:
            if find(student1) != find(student2):
                union(student1, student2)
cache = find(1)
res = [i for i in range(n + 1) if find(i) == cache]
print(len(res))
print(*sorted(res))