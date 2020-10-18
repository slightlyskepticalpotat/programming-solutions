import collections

def bfs(start):
    searched, queue = [], collections.deque([start])
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if thing not in searched and plan[thing[0]][thing[1]] != 'X': # validation
                searched.append(thing)
                queue += [thing]
                dist[thing] = dist.get(searching, 0) + 1

def peers(x, y):
    peers = []
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append((x + 1, y))
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append((x - 1, y))
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append((x, y + 1))
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append((x, y - 1))
    return peers

plan = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'], [' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' '], [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' '], ['X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']]
rows, columns, dist = 10, 10, {}
x, y = map(int, input().split())

bfs((9, 0))
print(f"Betty will sweat {dist[(9 - y + 1, x - 1)]}mL to get to her candy cane")