import sys
from collections import deque

input = sys.stdin.readline

def peers(x, y):
    peers = []
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append((x, y + 1))
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append((x, y - 1))
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append((x + 1, y))
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append((x - 1, y))
    if 0 <= x + 1<= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append((x + 1, y + 1))
    if 0 <= x + 1<= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append((x + 1, y - 1))
    if 0 <= x - 1 <= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append((x - 1, y + 1))
    if 0 <= x - 1 <= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append((x - 1, y - 1))
    return peers

def bfs(start):
    searched, queue = [], deque([start])
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if thing not in searched and plan[thing[0]][thing[1]] != '#': # validation
                searched.append(thing)
                queue += [thing]
                dist[thing] = dist[searching] + 1

for _ in range(5):
    plan = []
    for i in range(8):
        plan.append([char for char in input().strip()])

    rows, columns, dist = 8, 8, {}
    for i in range(rows):
        for j in range(columns):
            dist[(i, j)] = 0

    for i in range(rows):
        for j in range(columns):
            if plan[i][j] == "A":
                start = (i, j)
                continue
            if plan[i][j] == "B":
                end = (i, j)

    bfs(start)
    print(dist[end])