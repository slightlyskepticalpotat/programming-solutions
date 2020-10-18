import sys

input = sys.stdin.readline

def peers(x, y):
    neighbours = 0
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1 and board[x + 1][y] == "X":
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1 and board[x - 1][y] == "X":
        neighbours += 1
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x][y + 1] == "X":
        neighbours += 1
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x][y - 1] == "X":
        neighbours += 1
    if 0 <= x + 1 <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x + 1][y + 1] == "X":
        neighbours += 1
    if 0 <= x + 1 <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x + 1][y - 1] == "X":
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y + 1 <= columns - 1 and board[x - 1][y + 1] == "X":
        neighbours += 1
    if 0 <= x - 1 <= rows - 1 and 0 <= y - 1 <= columns - 1 and board[x - 1][y - 1] == "X":
        neighbours += 1
    return neighbours

rows, columns = map(int, input().split())
board = [[char for char in input().strip()] for  _ in range(rows)]

for i in range(1, 101):
    new = [["."] * columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            neighbours = peers(r, c)
            if board[r][c] == ".": # dead cell
                if neighbours == 3:
                    new[r][c] = "X"
            else: # live cell
                if neighbours == 2 or neighbours == 3:
                    new[r][c] = "X"
    board = new
    if i in [1, 5, 10, 50, 100]:
        print(sum(line.count("X") for line in board))
# Don't Panic.