import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    searched.append(start)
    while queue:
        searching = queue.popleft()
        for thing in book[searching]:
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
                dist[thing] = dist[searching] + 1
    return None

input = sys.stdin.readline
pages = int(input())
searched = []
endings = []
ending = float("inf")
book = {}
dist = {}
valid = True
for i in range(1, pages + 1): # compensate for arrays starting at 0
    dist[i] = 0
    branch = [int(i) for i in input().split()]
    if branch == [0]:
        book[i] = []
        endings.append(i)
    else:
        book[i] = branch[1:]

bfs(1)
for thing in book.keys(): # check if book is valid
    if dist[thing] == 0 and thing != 1:
        valid = False
print("Y") if valid == True else print("N") # fancy inline if/else
for thing in endings:
    if thing in searched and dist[thing] + 1 < ending:
        ending = dist[thing] + 1
print(ending)