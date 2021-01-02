import sys

input = sys.stdin.readline

def recurse(x, y, searched):
    if (x, y) in searched:
        return float("inf")
    if type(spreadsheet[x][y]) == list:
        value = 0
        for cell in spreadsheet[x][y]:
            value += recurse(ord(cell[0]) - 65, int(cell[1:]) - 1, searched + [(x, y)])
        spreadsheet[x][y] = value
        return value
    return spreadsheet[x][y]

spreadsheet, searched = [[i for i in input().strip().split()] for _ in range(10)], []
for i in range(10):
    for j in range(9):
        try:
            spreadsheet[i][j] = int(spreadsheet[i][j])
        except:
            spreadsheet[i][j] = spreadsheet[i][j].split("+")
for i in range(10):
    for j in range(9):
        if type(spreadsheet[i][j]) == list:
            spreadsheet[i][j] = recurse(i, j, [])
for i in range(10):
    for j in range(9):
        if spreadsheet[i][j] > 1000000000:
            spreadsheet[i][j] = "*"
for i in range(10):
    print(*spreadsheet[i])