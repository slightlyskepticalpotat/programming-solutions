import sys

input = sys.stdin.readline

def dfs(start):
    stack = [start]
    searched.add(start)
    while stack and len(searched) < free - k:
        x, y = stack.pop()
        if (x, y) not in searched:
            searched.add((x, y))
        if 0 <= x + 1 < n and 0 <= y < m and plan[x + 1][y] == "." and (x + 1, y) not in searched:
            stack.append((x + 1, y))
        if 0 <= x - 1 < n and 0 <= y < m and plan[x - 1][y] == "." and (x - 1, y) not in searched:
            stack.append((x - 1, y))
        if 0 <= x < n and 0 <= y + 1 < m and plan[x][y + 1] == "." and (x, y + 1) not in searched:
            stack.append((x, y + 1))
        if 0 <= x < n and 0 <= y - 1 < m and plan[x][y - 1] == "." and (x, y - 1) not in searched:
            stack.append((x, y - 1))

n, m, k = map(int, input().split())
plan, free, searched = [[i for i in input().strip()] for j in range(n)], 0, set()
for i in range(n):
    for j in range(m):
        if plan[i][j] == ".":
            start = (i, j)
            free += 1
dfs(start)
for i in range(n):
    for j in range(m):
        if plan[i][j] == "." and (i, j) not in searched and k:
            plan[i][j] = "X"
            k -= 1
for i in range(n):
    print("".join(plan[i]))
