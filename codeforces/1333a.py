import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [["B" for i in range(m)] for j in range(n)]
    grid[0][0] = "W"
    print("\n".join("".join(i) for i in grid))