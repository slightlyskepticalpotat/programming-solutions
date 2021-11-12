import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 ** 16)

def peers(x):
    peers, colour = [], plan[x[0]][x[1]]
    if 0 <= x[0] + 1 < n and plan[x[0] + 1][x[1]] == colour:
        peers.append((x[0] + 1, x[1]))
    if 0 <= x[0] - 1 < n and plan[x[0] - 1][x[1]] == colour:
        peers.append((x[0] - 1, x[1]))
    if 0 <= x[1] + 1 < m and plan[x[0]][x[1] + 1] == colour:
        peers.append((x[0], x[1] + 1))
    if 0 <= x[1] - 1 < m and plan[x[0]][x[1] - 1] == colour:
        peers.append((x[0], x[1] - 1))
    return peers

def dfs(start, last):
    if start in searched:
        global flag
        flag = True
        return
    searched.add(start)
    for peer in peers(start):
        if peer != last:
            dfs(peer, start)

n, m = map(int, input().split())
plan, searched, flag = [[char for char in input().strip()] for _ in range(n)], set(), False
for i in range(n):
    for j in range(m):
        if (i, j) not in searched:
            dfs((i, j), (-1, -1))
            
if flag:
    print("Yes")
else:
    print("No")
