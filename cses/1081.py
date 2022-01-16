import sys

input = sys.stdin.readline

n, values = int(input()), [int(i) for i in input().split()]
cnt = [0 for i in range(1000001)]
for i in values:
    cnt[i] += 1
for i in range(1000000, -1, -1): # loop through possible x
    muls = 0
    for j in range(i, 1000001, i):
        muls += cnt[j]
    if muls > 1:
        print(i)
        raise SystemExit
