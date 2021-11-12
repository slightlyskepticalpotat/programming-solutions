import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x, m = map(int, input().split())
    l, r = x, x
    for i in range(m):
        li, ri = map(int, input().split())
        if max(l, li) <= min(r, ri): # if they intersect
            l = min(l, li)
            r = max(r, ri)
    print(r - l + 1)