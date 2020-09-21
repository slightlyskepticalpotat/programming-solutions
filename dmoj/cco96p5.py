import sys

input = sys.stdin.readline

def dfs_all_paths(start, end, graph, path = []):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for vertex in graph[start]:
        if vertex not in path:
            extended_paths = dfs_all_paths(vertex, end, graph, path)
            for path in extended_paths:
                paths.append(path)
    return paths

roads = {}
m, n = map(int, input().strip().split())
for _ in range(m):
    a, b = input().strip().split()
    if a in roads.keys():
        if b in roads.keys():
            roads[a].append(b)
            roads[b].append(a)
        else:
            roads[a].append(b)
            roads[b] = [a]
    else:
        if b in roads.keys():
            roads[a] = [b]
            roads[b].append(a)
        else:
            roads[a] = [b]
            roads[b] = [a]

for _ in range(n):
    a, b = input().strip().split()
    paths = dfs_all_paths(a, b, roads)
    shortest = sorted(paths, key = lambda x: len(x))[0]
    print("".join([i[0] for i in shortest]))