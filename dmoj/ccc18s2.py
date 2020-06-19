import sys
input = sys.stdin.readline

grid = int(input())
flowers = []

for i in range(grid):
    flowers.append([int(i) for i in input().split()])

for i in range(0, 4):
    flag = 1
    for i in range(grid):
        if flowers[i] == sorted(flowers[i]):
            for j in range(grid):

                if flowers[-1][j] > flowers[0][j]:
                    flag = 0
                else:
                    flag = 1
                    break

    if flag == 0:
        for i in range(grid):
            for j in range(grid):
                print(flowers[i][j], end=" ")
            print("")

    flowers = list(zip(*flowers[::-1]))
    flowers = [list(i) for i in flowers]