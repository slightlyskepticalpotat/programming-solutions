# https://dmoj.ca/problem/ccc03s3
import sys
from collections import deque

input = sys.stdin.readline
plan = []
rooms = []
flooring = int(input())
rows = int(input())
columns = int(input())
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
                plan[thing[0]][thing[1]] = "I"
                queue += [thing]
                size+=1
    return size

for i in range(rows):
    for j in range(columns):
        if plan[i][j] == ".":
            plan[i][j] = "I"
            x = [i, j]
            rooms.append(size(x))

rooms.sort(reverse=True)
rooms_floored = 0

for thing in rooms:
    if flooring >= thing:
        rooms_floored+=1
        flooring-=thing
    else:
        break
if rooms_floored == 1:
    print("1 room, {} square metre(s) left over".format(flooring))
else:
    print("{} rooms, {} square metre(s) left over".format(rooms_floored, flooring))