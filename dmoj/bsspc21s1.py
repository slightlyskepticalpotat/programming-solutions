import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid, possible = [[i for i in input().strip()] for j in range(n)], True
for i in range(n):
    for j in range(m):
        if grid[i][j] != ".":
            if grid[i][m - j - 1] != grid[i][j]:
                if grid[i][m - j - 1] != ".":
                    possible = False
                else:
                    grid[i][m - j - 1] = grid[i][j]
            if grid[n - i - 1][j] != grid[i][j]:
                if grid[n - i - 1][j] != ".":
                    possible = False
                else:
                    grid[n - i - 1][j] = grid[i][j]
            if grid[n - i - 1][m - j - 1] != grid[i][j]:
                if grid[n - i - 1][m - j - 1] != ".":
                    possible = False
                else:
                    grid[n - i - 1][m - j - 1] = grid[i][j]
for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            grid[i][j] = "z"
if possible:
    for row in grid:
        print("".join(row))
else:
    print(-1)