import bisect, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, w = map(int, input().split())
    values, loc = sorted([int(i) for i in input().split()], reverse=True), []
    for value in values:
        i = bisect.bisect_left(loc, value) # biggest i > value in loc
        if i < len(loc):
            loc[i] -= value
        else:
            loc.append(w - value)
    print(len(loc))
