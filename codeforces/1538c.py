import bisect, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    vals = list(sorted([int(i) for i in input().split()]))
    print(sum([bisect.bisect_right(vals, r - vals[i], i + 1, n) - bisect.bisect_left(vals, l - vals[i], i + 1, n) for i in range(n)]))
