import sys
input = sys.stdin.readline

number = int(input())
acorns = sorted([int(i) for i in input().split()], reverse=True)
ree = []

for i in range(len(acorns)):
    buff = [acorns[i]]
    for j in range(len(acorns)):
        if acorns[j] < acorns[i] and acorns[j] not in buff:
            buff.append(acorns[j])
            acorns[j] = 0
    ree.append(buff)
print(sum([max(i) for i in ree]))