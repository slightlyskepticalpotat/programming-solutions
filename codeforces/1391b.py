import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [[i for i in input().strip()] for j in range(n)]
    print(sum([grid[n - 1][i] == "D" for i in range(m)]) + sum([grid[i][m - 1] == "R" for i in range(n)]))
