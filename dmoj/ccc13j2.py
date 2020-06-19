sign = input()
yes = 0

for char in sign:
    if char != 'I' and char != 'O' and char != 'S' and char != 'H' and char != 'Z' and char != 'X' and char != 'N':
        yes = 0
        break
    else:
        yes = 1
if yes == 0:
    print('NO')
else:
    print('YES')