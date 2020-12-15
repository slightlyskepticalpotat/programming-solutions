import sys

input = sys.stdin.readline

f, r = map(int, input().split())
cds = []
for i in range(f):
    floor = [int(i) for i in input().split()]
    cd = [0]
    for i in range(r):
        cd.append(cd[i] + floor[i])
    cds.append(cd)

for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(cds[c - 1][b] - cds[c - 1][a - 1])