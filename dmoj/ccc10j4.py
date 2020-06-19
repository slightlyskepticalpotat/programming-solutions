# please dm me on discord if you see this, along with a short explanation of why you're stalking my submissions
# https://dmoj.ca/problem/ccc10j4

import sys, math
input = sys.stdin.readline

def pattern(ree):
    for i in range(math.ceil(len(temp)-2/ree)):
        for j in range(ree):
            if ree*i+j>=(len(temp)-2):
                return 1
            if(diff[ree*i+j] != diff[j]):
                return -1
    return 1

answers = []
backup = []
        
while True:
    temp = input().strip().split(' ')
    temp = [int(i) for i in temp]
    diff = []
    backup.append(temp)

    if len(temp) == 1 and temp[0] == 0:
        break
    elif temp[0] == 1 and temp [1] == 0:
        answers.append(0)
    else:
        for i in range(1,len(temp)-1):
            diff.append(temp[i+1]-temp[i])
        for i in range(1,len(temp)-1):
            if pattern(i) == 1:
                answers.append(i)
                break
            
for i in range(0, len(answers)):
    print(answers[i])