# (0, 2) (1, 2) (2, 2)
# (0, 1) (1, 1) (2, 1)
# (0, 0) (1, 0) (2, 0)

import sys, collections
input = sys.stdin.readline

def peers(x, y):
    peers = []
    if plan[x][y] == "+":
        if 0 <= x < c and 0 <= y + 1 < r and plan[x][y + 1] != "*":
            peers.append((x, y + 1))
        if 0 <= x < c and 0 <= y - 1 < r and plan[x][y - 1] != "*":
            peers.append((x, y - 1))
        if 0 <= x + 1 < c and 0 <= y < r and plan[x + 1][y] != "*":
            peers.append((x + 1, y))
        if 0 <= x - 1 < c and 0 <= y < r and plan[x - 1][y] != "*":
            peers.append((x - 1, y))
    elif plan[x][y] == "-":
        if 0 <= x + 1 < c and 0 <= y < r and plan[x + 1][y] != "*":
            peers.append((x + 1, y))
        if 0 <= x - 1 < c and 0 <= y < r and plan[x - 1][y] != "*":
            peers.append((x - 1, y))
    elif plan[x][y] == "|":
        if 0 <= x < c and 0 <= y + 1 < r and plan[x][y + 1] != "*":
            peers.append((x, y + 1))
        if 0 <= x < c and 0 <= y - 1 < r and plan[x][y - 1] != "*":
            peers.append((x, y - 1))
    else:
        pass
    return peers

def pathing(start):
    searched = [start]
    queue = collections.deque()
    queue += [start]
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
                dist[tuple(thing)] = dist[tuple(searching)] + 1

for i in range(int(input())):
    plan, dist = [], {}
    r, c = int(input()), int(input())
    for i in range(r):
        plan.append(list(input().strip()))
    for i in range(c):
        for j in range(r):
            dist[(i, j)] = 1
    plan = list(zip(*plan[::-1])) # rotating is good, proper coordinates is bad
    pathing((0, r - 1))
    if dist[(c - 1, 0)] == 1 and (0, r - 1) != (c - 1, 0):
        print(-1)
    else:
        print(dist[(c - 1, 0)])