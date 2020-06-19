wins = 0
for i in range(0,6):
    if input() == 'W':
        wins+=1
    else:
        pass
if wins == 5 or wins == 6:
    print('1')
elif wins == 4 or wins == 3:
    print('2')
elif wins == 2 or wins == 1:
    print('3')
else:
    print('-1')