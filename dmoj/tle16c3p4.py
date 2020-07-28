rows, columns = int(input()), int(input())

if rows == 1 or columns == 1:
    print("First")
elif (rows + columns) % 2 == 1: # potential moves
    print("First")
else:
    print("Second")