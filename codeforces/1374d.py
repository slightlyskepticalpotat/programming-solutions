import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    vals, cnts = [int(i) for i in input().split()], {}
    for i in vals:
        if i % k: # if not divisible
            cnts[k - i % k] = cnts.get(k - i % k, 0) + 1 # remaining
    if cnts:
        best = max(cnts, key = lambda x: (cnts[x], x))
        print(k * (cnts[best] - 1) + best + 1)
    else: # everything already divisible
        print(0)
