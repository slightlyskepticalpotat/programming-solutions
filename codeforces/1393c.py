import sys

input = sys.stdin.readline

for _ in range(int(input())):
    cnt, vals = [0 for _ in range(int(input()) + 1)], [int(i) for i in input().split()]
    for i in vals:
        cnt[i] += 1
    n, m, c = len(vals), max(cnt), cnt.count(max(cnt))
    print((n - m * c) // (m - 1) + (c - 1)) # not-max cakes // spaces between max cakes + other max cakes in between
