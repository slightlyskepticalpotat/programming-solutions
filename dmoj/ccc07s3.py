import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(65536)

def dfs(start, end, path = None):
    if path == None:
        path = []
    path += [start]
    if start == end:
        return path
    if start in friends.keys(): # validate input
        if friends[start] not in path:
            extended_path = dfs(friends[start], end, path)
            if extended_path:
                return extended_path
    return None
    
friends = {}
for i in range(int(input())):
    a, b = map(int, input().split())
    friends[a] = b

while True:
    a, b = map(int, input().split())
    if a | b == 0:
        break
    result = dfs(a, b)
    if result:
        print("Yes", len(result) - 2) # account for start and end
    else:
        print("No")