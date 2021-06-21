import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    new, vals, best = sorted([i for i in vals if i <= 0]), sorted([i for i in vals if i > 0]), float("inf") # divide into positive and negative
    for i in range(len(new) - 1): # find minimum difference
        best = min(best, new[i + 1] - new[i])
    if (vals and vals[0] <= best) or not new:
        new.append(vals[0]) # add positive if possible
    print(len(new))
