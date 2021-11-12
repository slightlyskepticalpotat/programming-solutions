import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    plan = [[int(i) for i in input().split()] for j in range(n)]
    for i in range(n):
        for j in range(m): # alternate the parity like a chessboard
                plan[i][j] += (i % 2 + j % 2 + plan[i][j] % 2) % 2
    for i in range(n):
        print(*plan[i])
