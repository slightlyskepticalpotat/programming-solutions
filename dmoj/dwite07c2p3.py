import sys
from collections import deque

def peers(x, y): # go in 4 directions 
    peers = []
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append([x, y + 1])
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append([x, y - 1])
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append([x + 1, y])
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append([x - 1, y])
    return peers

def size(start): # size of each room
    searched = []
    size = 1
    queue = deque([start])
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if thing not in searched:
                if plan[thing[0]][thing[1]] == ".":
                    searched.append(thing)
                    plan[thing[0]][thing[1]] = "#"
                    queue += [thing]
                    size += 1
    return size

input = sys.stdin.readline
plan = []
rows, columns = int(input()), int(input())
for i in range(rows):
    plan.append([i for i in input().strip()])

for i in range(1, 6):
    for j in range(len(plan)):
        for k in range(len(plan[j])):
            if plan[j][k] == str(i):
                print(size([j, k]))