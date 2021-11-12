import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [[int(i) for i in input().split()] for _ in range(n)]
    row_free = [i for i in range(n) if not any(grid[i])]
    grid = [list(row) for row in zip(*grid[::-1])]
    col_free = [i for i in range(m) if not any(grid[i])]
    if min(len(row_free), len(col_free)) % 2:
        print("Ashish")
    else:
        print("Vivek")