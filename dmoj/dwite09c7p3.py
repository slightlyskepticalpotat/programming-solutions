from collections import deque

def peers(x, y):
    peers = []
    if 0 <= x <= 9 and 0 <= y + 1 <= 9:
        peers.append([x, y + 1])
    if 0 <= x <= 9 and 0 <= y - 1 <= 9:
        peers.append([x, y - 1])
    if 0 <= x + 1 <= 9 and 0 <= y <= 9:
        peers.append([x + 1, y])
    if 0 <= x - 1 <= 9 and 0 <= y <= 9:
        peers.append([x - 1, y])
    return peers

def size(start):
    searched, size = [start], 1
    queue = deque([start])
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if plan[thing[0]][thing[1]] == "#" and thing not in searched:
                searched.append(thing)
                queue += [thing]
                size += 1
    return size

for i in range(5):
    plan = [[i for i in input().strip()] for j in range(10)]
    for j in range(10):
        for k in range(10):
            if plan[j][k] == "A":
                print(size([j, k]))
    placeholder = input().strip() # divider