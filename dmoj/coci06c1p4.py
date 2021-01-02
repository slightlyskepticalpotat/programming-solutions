import collections, sys

input = sys.stdin.readline

def bfs(start):
    searched, queue = set([start]), collections.deque([start])
    dist[start] = 0
    while queue:
        searching = queue.popleft()
        for peer in peers(searching):
            if peer not in searched and dist[searching] + 1 < flooded_dist[peer] and plan[peer[0]][peer[1]] != "X":
                searched.add(peer)
                queue += [peer]
                dist[peer] = dist[searching] + 1

def flooded_bfs(start):
    searched, queue = set([start]), collections.deque([start])
    flooded_dist[start] = 0
    while queue:
        searching = queue.popleft()
        for peer in peers(searching):
            if peer not in searched and plan[peer[0]][peer[1]] == ".":
                searched.add(peer)
                queue += [peer]
                flooded_dist[peer] = min(flooded_dist[peer], flooded_dist[searching] + 1)

def peers(x):
    peers = []
    if 0 <= x[0] + 1 < r:
        peers.append((x[0] + 1, x[1]))
    if 0 <= x[0] - 1 < r:
        peers.append((x[0] - 1, x[1]))
    if 0 <= x[1] + 1 < c:
        peers.append((x[0], x[1] + 1))
    if 0 <= x[1] - 1 < c:
        peers.append((x[0], x[1] - 1))
    return peers

r, c = map(int, input().split())
plan = [[char for char in input().strip()] for _ in range(r)]
start, stop, initial, flooded_dist, dist = 0, 0, [], {}, {}
for i in range(r):
    for j in range(c):
        if plan[i][j] == "S":
            start = (i, j)
        elif plan[i][j] == "D":
            stop = (i, j)
        elif plan[i][j] == "*":
            initial.append((i, j))
        flooded_dist[(i, j)] = float("inf")
        dist[(i, j)] = -1

for square in initial:
    flooded_bfs(square)
bfs(start)
if dist[stop] == -1:
    print("KAKTUS")
else:
    print(dist[stop])