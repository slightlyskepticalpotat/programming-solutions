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

n, m, q, c = map(int, input().split())
graph, dist = {i + 1: [] for i in range(n)}, {i + 1: -1 for i in range(n)}
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(c)
for i in range(q):
    a, b = map(int, input().split())
    if dist[a] == -1 or dist[b] == -1:
        print("This is a scam!")
    else:
        print(dist[a] + dist[b])