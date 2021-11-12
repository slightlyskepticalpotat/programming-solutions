import sys

input = sys.stdin.readline

for _ in range(int(input())):
    rect, x, y = [[i for i in input().strip()] for j in range(int(input()))], [], []
    for i in range(len(rect)):
        for j in range(len(rect[0])):
            if rect[i][j] == "*":
                if i not in x:
                    x.append(i)
                if j not in y:
                    y.append(j)
    if min(len(x), len(y)) == 2: # diagonal
        rect[x[0]][y[1]], rect[x[1]][y[0]] = "*", "*"
    else:
        if len(x) == 1:
            if 0 <= x[0] - 1 <= len(rect):
                rect[x[0] - 1][y[0]] = "*"
                rect[x[0] - 1][y[1]] = "*"
            else:
                rect[x[0] + 1][y[0]] = "*"
                rect[x[0] + 1][y[1]] = "*"
        else:
            if 0 <= y[0] - 1 <= len(rect[0]):
                rect[x[0]][y[0] - 1] = "*"
                rect[x[1]][y[0] - 1] = "*"
            else:
                rect[x[0]][y[0] + 1] = "*"
                rect[x[1]][y[0] + 1] = "*"
    for row in rect:
        print("".join(row))
