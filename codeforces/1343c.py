import copy, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, pos, neg = int(input()), [int(i) for i in input().split()], [], []
    loc, curr = [], 1
    for i in range(n):
        if (curr == 1 and vals[i] > 0) or (curr == -1 and vals[i] < 0):
            loc.append(vals[i])
        elif ((curr == 1 and vals[i] < 0) or (curr == -1 and vals[i] > 0)) and loc:
            pos.append(max(loc))
            loc, curr = [vals[i]], curr * -1
    if loc: # last element
        pos.append(max(loc))

    loc, curr = [], -1
    for i in range(n):
        if (curr == 1 and vals[i] > 0) or (curr == -1 and vals[i] < 0):
            loc.append(vals[i])
        elif ((curr == 1 and vals[i] < 0) or (curr == -1 and vals[i] > 0)) and loc:
            neg.append(max(loc))
            loc, curr = [vals[i]], curr * -1
    if loc: # last element
        neg.append(max(loc))

    if len(pos) == len(neg):
        print(max(sum(pos), sum(neg)))
    elif len(pos) > len(neg):
        print(sum(pos))
    elif len(pos) < len(neg):
        print(sum(neg))