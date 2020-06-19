scale = int(input())

diagram1 = ['*','x','*']
diagram2 = [' ','x','x']
diagram3 = ['*',' ','*']

for i in range(0,scale):
    print((diagram1[0]*scale)+(diagram1[1]*scale)+(diagram1[2]*scale))
for i in range(0,scale):
    print((diagram2[0]*scale)+(diagram2[1]*scale)+(diagram2[2]*scale))
for i in range(0,scale):
    print((diagram3[0]*scale)+(diagram3[1]*scale)+(diagram3[2]*scale))