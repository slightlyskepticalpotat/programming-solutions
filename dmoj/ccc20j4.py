import sys
input = sys.stdin.readline

text = input()
string = input()
shifts = []
flag = 0

for i in range(0, len(string)-1):
    shifts.append(string[i:-1]+string[0:i])

for i in shifts:
    if i in text:
        print('yes')
        flag = 1
        break
    
if flag == 0:
    print('no')
else:
    pass