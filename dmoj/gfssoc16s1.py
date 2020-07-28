import sys
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    searched = [start]
    while queue:
        searching = queue.popleft()
        for thing in graph[searching]:
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
                dist[thing] = dist[searching] + 1
    return None

input = sys.stdin.readline

stops = {"home": [], "Waterloo GO": []}
dist = {"home": 0, "Waterloo GO": 0} 
destinations, transfers = map(int, input().split())
for i in range(destinations):
    destination = input().strip()
    stops[destination] = []
    dist[destination] = 0
for i in range(transfers):
    a, b = input().strip().split("-")
    stops[a].append(b)
    stops[b].append(a)

bfs("home", stops)
if dist["Waterloo GO"] == 0:
    print("RIP ACE")
else:
    print(dist["Waterloo GO"])