# range updates with difference arrays

import sys

input = sys.stdin.readline

n, h = map(int, input().split())
da = [0 for i in range(h + 1)] # cave[0] = top of cave

for i in range(n):
    x = int(input())
    if i % 2:
        da[0] += 1
        da[x] -= 1
    else:
        da[-1] -= 1
        da[h - x] += 1

cave = [0 for i in range(h)]
cave[0] = da[0]
for i in range(1, h):
    cave[i] = cave[i - 1] + da[i]
smallest = min(cave)
print(smallest, cave.count(smallest))