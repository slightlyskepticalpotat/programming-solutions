import sys

input = sys.stdin.readline

nice = []
for i in range(1, 31):
    j = 2 ** i - 1 # to fill highest step
    nice.append((j * (j + 1)) // 2) # total number of blocks

for _ in range(int(input())): # all nice staircases must have n steps
    x, n, tot = int(input()), 0, 0
    for i in nice:
        if tot + i <= x:
            tot += i
            n += 1
    print(n)
