square = 1

while True:
    
    move = int(input())
    
    if move == 0:
        print('You Quit!')
        break
    else:
        square = square + move
    
    if square == 54:
        square = 19
    elif square == 90:
        square = 48
    elif square == 99:
        square = 77
    elif square == 9:
        square = 34
    elif square == 40:
        square = 64
    elif square == 67:
        square = 86
    
    
    if square > 100:
        square = square - move
    print('You are now on square %s' % square)
  
    if square == 100:
        print('You Win!')
        break