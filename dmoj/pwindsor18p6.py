import collections, sys

input = sys.stdin.readline

def bfs(start):
    searched, queue = set([start]), collections.deque([start])
    dist[start] = 0
    while queue:
        searching = queue.popleft()
        for thing in graph[searching]:
            if thing not in searched:
                searched.add(thing)
                queue += [thing]
                dist[thing] = dist[searching] + 1

n, m, a, b = map(int, input().split())
graph, dist = {i + 1: [] for i in range(n)}, {i + 1: -1 for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
bfs(a)
if dist[1] == -1 or dist[b] == -1:
    print(-1)
else:
    print(dist[1] + dist[b])