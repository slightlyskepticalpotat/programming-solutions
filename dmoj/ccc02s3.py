import sys

input = sys.stdin.readline

backyard, moves = [], []
r, c = int(input()), int(input())
for i in range(r):
    backyard.append([char for char in input().strip()])

for i in range(int(input())):
    moves.append(input().strip())

for i in range(r):
    for j in range(c):
        if backyard[i][j] != "X": # is starting square valid?
            for k in range(4): # 0 == 0, 1 == 90, 2 == 180, 3 == 270
                x, y, d = i, j, k
                flag = True
                for thing in moves:
                    if thing == "L":
                        d = (d - 1) % 4
                    elif thing == "R":
                        d = (d + 1) % 4
                    elif thing == "F":
                        if d == 0:
                            y += 1
                        elif d == 1:
                            x += 1
                        elif d == 2:
                            y -= 1
                        elif d == 3:
                            x -= 1
                    try:
                        if x < 0 or x >= r or y < 0 or y >= c or backyard[x][y] == "X": # is the ending square valid?
                            flag = False
                            break
                    except:
                        flag = False
                        break
                if flag:
                    backyard[x][y] = "*"

for line in backyard:
    print("".join(line))