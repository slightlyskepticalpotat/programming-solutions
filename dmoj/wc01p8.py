# union-find data structure

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

for _ in range(int(input())):
    n, c = map(int, input().split()) # nodes, edges
    edges, ans = sorted([[int(i) for i in input().split()] for _ in range(c)], key = lambda x: x[2]), 0
    path, size = [i for i in range(n + 1)], [1 for i in range(n + 1)]
    for i in range(c):
        if find(edges[i][0]) != find(edges[i][1]):
            union(edges[i][0], edges[i][1])
            ans += edges[i][2]
    try:
        for i in range(1, n):
            if find(i) != find(i + 1):
                print("Requires more conduits")
                raise
        print(ans)
    except:
        pass