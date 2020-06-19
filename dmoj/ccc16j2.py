row1 = []
row2 = []
row3 = []
row4 = []

a, b, c, d = input().split()
row1.append(int(a))
row1.append(int(b))
row1.append(int(c))
row1.append(int(d))

a, b, c, d = input().split()
row2.append(int(a))
row2.append(int(b))
row2.append(int(c))
row2.append(int(d))

a, b, c, d = input().split()
row3.append(int(a))
row3.append(int(b))
row3.append(int(c))
row3.append(int(d))

a, b, c, d = input().split()
row4.append(int(a))
row4.append(int(b))
row4.append(int(c))
row4.append(int(d))

if (sum(row1) == sum(row2) == sum(row3) == sum(row4)) and row1[0] + row1[1] + row1[2] + row1[3] == row2[0] + row2[1] + row2[2] + row2[3]:
    print('magic')
else:
    print('not magic')