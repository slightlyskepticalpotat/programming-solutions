import sys

input = sys.stdin.readline

graph, leaves = {i + 1: [] for i in range(int(input()))}, []
dist, queue, second = {i + 1: 0 for i in range(len(graph))}, [], set()
for _ in range(len(graph) - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    if len(graph[node]) == 1:
        leaves.append(node)
queue.append(1)
while queue: # bfs
    searching = queue.pop()
    for peer in graph[searching]:
        if not dist[peer]:
            dist[peer] = dist[searching] + 1
            queue.append(peer)
if len(set([dist[node] % 2 for node in leaves])) == 1:
    minimum = 1
else:
    minimum = 3

for leaf in leaves:
    for peer in graph[leaf]:
        second.add(peer)
maximum = len(graph) - 1 - len(leaves) + len(second)

print(minimum, maximum)