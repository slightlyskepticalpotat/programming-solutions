import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    vals = [i for i in range(n) if vals[i] != i + 1] # out of order ones
    if not vals: # do nothing if sorted
        print(0)
    elif vals[-1] - vals[0] + 1 == len(vals): # we can sort in 1 pass
        print(1)
    else: # we can sort in 2 passes
        print(2)
