import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s, side, yes, counts = input().strip(), [set() for _ in range(k)], True, [0, 0] # every 1, 2, 3 ... k must be the same
    for i in range(n):
        if s[i] != "?":
            side[i % k].add(s[i])
    for i in range(k):
        if len(side[i]) > 1:
            yes = False
        elif side[i]:
            counts[int(side[i].pop())] += 1
    print(f"{'YES' if yes and max(counts) <= k // 2 else 'NO'}") # something new
