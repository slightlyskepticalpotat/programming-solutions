import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    searched = [start]
    queue = deque([start])
    while queue:
        searching = queue.popleft()
        if searching == end:
            return True
        for thing in graph[searching]:
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
    return False
                
target, edges = map(int, input().split())
graph = {}
edges_list = []
for i in range(1, target + 1):
    graph[i] = []
for i in range(edges):
    a, b = map(int, input().split())
    edges_list.append([a, b])
    graph[a].append(b)

for thing in edges_list:
    graph[thing[0]].remove(thing[1])
    if bfs(1, target) == True:
        print("YES")
    else:
        print("NO")
    graph[thing[0]].append(thing[1])