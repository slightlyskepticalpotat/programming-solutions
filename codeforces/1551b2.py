import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    vals, cnt, to_colour, colours = [int(i) for i in input().split()], {i + 1: 0 for i in range(n)}, [], [0 for i in range(n)]
    for i in vals:
        cnt[i] += 1
    cnt = {i: min(k, cnt[i]) for i in cnt} # maximum times we can colour it
    for i in range(n):
        if cnt[vals[i]]:
            to_colour.append([i, vals[i]])
            cnt[vals[i]] -= 1
    to_colour = [i[0] for i in sorted(to_colour, key = lambda x: x[1])] # different colours for same value
    for i in range(len(to_colour) % k): # not enough colours
        to_colour.pop()
    for i in range(len(to_colour)):
        colours[to_colour[i]] = (i % k) + 1
    print(*colours)