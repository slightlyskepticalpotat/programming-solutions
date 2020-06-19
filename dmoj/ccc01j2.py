import sys
input = sys.stdin.readline

x = int(input())
m = int(input())
flag = 0

for i in range(0, 1000):
    if (x*i) % m == 1:
        print(i)
        flag = 1
        break
if flag == 1:
    pass
else:
    print('No such integer exists.')