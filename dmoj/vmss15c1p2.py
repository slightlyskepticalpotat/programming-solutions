# https://dmoj.ca/problem/ccc03s3
import sys
from collections import deque

input = sys.stdin.readline
plan = []
rooms = 0
rows, columns = map(int, input().strip().split())
for i in range(rows):
    plan.append([i for i in input().strip()] )
    
def peers(x, y):
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

def size(start):
    searched = []
    size = 1
    queue = deque()
    queue += [start]
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in peers(searching[0], searching[1]):
            if plan[thing[0]][thing[1]] == ".":
                searched.append(thing)
                plan[thing[0]][thing[1]] = "X"
                queue += [thing]

for i in range(rows):
    for j in range(columns):
        if plan[i][j] == ".":
            plan[i][j] = "X"
            x = [i, j]
            size(x)
            rooms+=1
print(rooms)