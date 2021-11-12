import sys

input = sys.stdin.readline

# modified union-find
def find(x):
    if x != path[x]:
        path[x] = find(path[x])
    return path[x]

def union(x, y):
    path[find(x)] = find(y)

n, m1, m2 = map(int, input().split())
path, ans = [i for i in range(n * 2 + 1)], []
for _ in range(m1):
    u, v = map(int, input().split())
    union(u, v)
for _ in range(m2):
    u, v = map(int, input().split())
    u, v = u + n, v + n
    union(u, v)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if find(i) != find(j) and find(i + n) != find(j + n):
            ans.append([i, j])
            union(i, j)
            union(i + n, j + n)
print(len(ans))
for edge in ans:
    print(*edge)