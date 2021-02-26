import collections

def peers(x, r, c):
    peers = []
    if 0 <= x[0] <= r - 1 and 0 <= x[1] + 1 <= c - 1:
        peers.append((x[0], x[1] + 1))
    if 0 <= x[0] <= r - 1 and 0 <= x[1] - 1 <= c - 1:
        peers.append((x[0], x[1] - 1))
    if 0 <= x[0] + 1 <= r - 1 and 0 <= x[1] <= c - 1:
        peers.append((x[0] + 1, x[1]))
    if 0 <= x[0] - 1 <= r - 1 and 0 <= x[1] <= c - 1:
        peers.append((x[0] - 1, x[1]))
    return peers

def bfs(dist, graph, start, r, c):
    searched, queue = set([start]), collections.deque([start])
    dist[start] = 1
    while queue:
        searching = queue.popleft()
        for peer in peers(searching, r, c):
            if peer not in searched and not graph[peer[0]][peer[1]]:
                searched.add(peer)
                queue.append(peer)
                dist[peer] = dist[searching] + 1
            if peer == (r - 1, c - 1):
                return dist

def solution(bunnies):
    r, c, best, old_dist, = len(bunnies), len(bunnies[0]), float("inf"), {}
    for i in range(r):
        for j in range(c):
            old_dist[(i, j)] = 0
    initial = bfs(old_dist, bunnies, (0, 0), r, c)
    try:
        best = min(best, initial[(r - 1, c - 1)])
    except:
        pass
    for i in range(r):
        for j in range(c):
            if bunnies[i][j]:
                bunnies[i][j] = 0
                try:
                    initial = bfs(old_dist, bunnies, (0, 0), r, c)
                    best = min(best, initial[(r - 1, c - 1)])
                except:
                    pass
                bunnies[i][j] = 1
    return best
