# this is so spaghetti I should start an italian restaurant
import sys
from collections import deque

input = sys.stdin.readline
plan = []
rows, columns = map(int, input().split())
for i in range(rows):
    plan.append(list(input().strip()))

def peers(x, y):
    peers = []
    try:
        if plan[x+1][y] != "X" and 0 <= x+1 <= rows:
            peers.append((y, x+1))
    except:
        pass
    try:
        if plan[x-1][y] != "X" and 0 <= x-1 <= rows:
            peers.append((y, x-1))
    except:
        pass
    try:
        if plan[x][y+1] != "X" and 0 <= y+1 <= columns:
            peers.append((y+1, x))
    except:
        pass
    try:
        if plan[x][y-1] != "X" and 0 <= y-1 <= columns:
            peers.append((y-1, x))
    except:
        pass
    return peers

def bfs(start):
    searched = []
    queue = deque()
    queue += [start]
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[1], searching[0]):
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
                dist[thing] = dist[searching] + 1
                if plan[thing[1]][thing[0]] == "e":
                    return


dist = {}
for i in range(rows):
    for j in range(columns):
        dist[(j, i)] = 0
        
for i in range(rows):
    for thing in plan[i]:
        if thing == "s":
            starting = (plan[i].index(thing), i)
        elif thing == "e":
            ending = (plan[i].index(thing), i)

bfs(starting)

if dist[ending] == 0:
    print("-1")
else:
    print(dist[ending]-1)