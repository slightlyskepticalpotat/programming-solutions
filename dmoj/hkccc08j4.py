import sys
input = sys.stdin.readline

def win(x):
    y = set(x)
    for i in range(3): # horizontal
        if y == set(board[i]):
            return True
    for i in range(3): # vertical
        if y == set([board[0][i], board[1][i], board[2][i]]):
            return True
    if x == board[0][0] == board[1][1] == board[2][2]: # diagonal
        return True
    if x == board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def valid(snapshot):
    if win("X") == True and win("O") == True:
        return False
    if abs(x-o) > 1 or o > x:
        return False
    if win("X") and x == o:
        return False
    if win("O") and x > o:
        return False
    return True
    
for i in range(int(input())):
    board = []
    raw_data = input().strip()
    x = raw_data.count("X")
    o = raw_data.count("O")
    board.append(list(raw_data[0:3]))
    board.append(list(raw_data[3:6]))
    board.append(list(raw_data[6:9]))
    if valid(board):
        print("yes")
    else:
        print("no")