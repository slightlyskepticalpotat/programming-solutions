size, queens = map(int, input().split())
board = [[False] * size for _ in range(size)]

for i in range(queens):
    row, column = map(lambda x: int(x) - 1, input().split())
    safe = 0
    for i in range(size):
        for j in range(size):
            if i == row:
                board[i][j] = True
            elif j == column:
                board[i][j] = True
            elif abs(i - row) == abs(j - column):
                board[i][j] = True
for thing1 in board:
    for thing2 in thing1:
        if thing2 == False:
            safe+=1
print(safe)