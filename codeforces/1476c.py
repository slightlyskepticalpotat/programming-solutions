import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, l, a, b, best, last, curr = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()], 0, 0, 0
    for i in range(1, n): # the idea is to extend the cycle, one stage at a time
        curr = 1 + l[i] + abs(a[i] - b[i])
        if a[i] != b[i]: # try extending the cycle
            curr = max(curr, 1 + l[i] + last - abs(a[i] - b[i]))
        best = max(best, curr)
        last = curr
    print(best)
