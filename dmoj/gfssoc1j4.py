import sys
input = sys.stdin.readline

def win(x):
    y = set(x)
    for i in range(3):
        if y == set(board[i]):
            return True
    for i in range(3):
        if y == set([board[0][i], board[1][i], board[2][i]]):
            return True
    if x == board[0][0] == board[1][1] == board[2][2]:
        return True
    if x == board[0][2] == board[1][1] == board[2][0]:
        return True
    return False
                
board = []
for i in range(3):
    board.append(list(input().strip()))
    
g = win("O")
t = win("X")

if g == True:
    if t == True:
        print("Error, redo")
    else:
        print("Griffy")
else:
    if t == True:
        print("Timothy")
    else:
        print("Tie")