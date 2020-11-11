import sys

input = sys.stdin.readline
n, k = map(int, input().split())
items, best = list(sorted([int(i) for i in input().split()])), 0
l, r = 0, 0

while r < n:
    if r - l + 1 > best and items[r] - items[l] <= k:
        best = r - l + 1
    if items[r] - items[l] < k:
        r += 1
    else:
        l += 1
print(best)