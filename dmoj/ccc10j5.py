from collections import deque
def peers(x):
    peers = []
    if 0 < x[0] + 1 < 9 and 0 < x[1] + 2 < 9:
        peers.append((x[0] + 1, x[1] + 2))
    if 0 < x[0] + 1 < 9 and 0 < x[1] - 2 < 9:
        peers.append((x[0] + 1, x[1] - 2))
    if 0 < x[0] - 1 < 9 and 0 < x[1] + 2 < 9:
        peers.append((x[0] - 1, x[1] + 2))
    if 0 < x[0] - 1 < 9 and 0 < x[1] - 2 < 9:
        peers.append((x[0] - 1, x[1] - 2))
    if 0 < x[0] + 2 < 9 and 0 < x[1] + 1 < 9:
        peers.append((x[0] + 2, x[1] + 1))
    if 0 < x[0] + 2 < 9 and 0 < x[1] - 1 < 9:
        peers.append((x[0] + 2, x[1] - 1))
    if 0 < x[0] - 2 < 9 and 0 < x[1] + 1 < 9:
        peers.append((x[0] - 2, x[1] + 1))
    if 0 < x[0] - 2 < 9 and 0 < x[1] - 1 < 9:
        peers.append((x[0] - 2, x[1] - 1))
    return peers

def pathing(start):
    queue = deque()
    queue+=[start]
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in peers(searching):
            if thing not in searched:
                searched.append(thing)
                queue+=[thing]
                dist[thing] = dist[searching] + 1

yeet = [int(i) for i in input().split()]
yote = [int(i) for i in input().split()]
yeet, yote = tuple(yeet), tuple(yote)
searched = []
dist = {}
for i in range(0, 8):
    for j in range(0, 8):
        square = (i+1, j+1)
        dist[square] = 0
pathing(yeet)
print(dist[yote])