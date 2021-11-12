import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    cnt = [0 for i in range(n + 1)]
    for i in vals:
        cnt[i] += 1
    a, b = len([1 for i in cnt if i]), max(cnt)
    print(max(min(a - 1, b), min(a, b - 1)))