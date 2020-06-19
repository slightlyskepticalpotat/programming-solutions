import sys
input = sys.stdin.readline
ree = []
for i in range(int(input())):
    ree.append(int(input()))
print(len(set(ree)))