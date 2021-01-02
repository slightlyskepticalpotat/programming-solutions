import sys

input = sys.stdin.readline

def dfs(start, end):
    if start == end:
        return 1
    local = 0
    for peer in graph[start]:
        if not dist[peer]:
            dist[peer] = dfs(peer, end)
        local += dist[peer]
    return local

n = int(input())
graph, dist = {i + 1: [] for i in range(n)}, {i + 1: 0 for i in range(n)}
while True:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    graph[a].append(b)
print(dfs(1, n))