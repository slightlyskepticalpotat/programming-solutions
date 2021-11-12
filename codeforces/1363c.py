import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    graph = {i + 1: [] for i in range(n)}
    for i in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    if n % 2 and len(graph[x]) > 1:
        print("Ashish")
    else:
        print("Ayush")