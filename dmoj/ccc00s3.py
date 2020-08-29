import sys, re
from collections import deque

input = sys.stdin.readline

def bfs(start, end, graph):
    searched, queue = [start], deque([start])
    while queue:
        searching = queue.popleft()
        if searching == end:
            return True
        for thing in graph[searching]:
            if thing not in searched:
                searched.append(thing)
                queue += [thing]
    return False
        
websites = {}
for i in range(int(input())):
    website = input().strip()
    websites[website] = []
    while True:
        line = input().strip()
        if "</HTML>" in line:
            break
        else:
            links = re.findall('''(?:<A HREF=\")([^>]*)(?:\">)''', line)
            if links:
                for thing in links:
                    websites[website].append(thing)
                    print(f"Link from {website} to {thing}")
while True:
    start = input().strip()
    if start == "The End":
        break
    else:
        end = input().strip()
    if bfs(start, end, websites) == True:
        print(f"Can surf from {start} to {end}.")
    else:
        print(f"Can't surf from {start} to {end}.")