import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 ** 16)  

def dfs(x):
    visited[x] = 1
    for peer in graph[x]:
        if not visited[peer]:
            dfs(peer)

n, m = map(int, input().split())
graph, visited = {i + 1: [] for i in range(n)}, [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, y = map(int, input().split())
dfs(x)
print(visited[y])