import sys

input = sys.stdin.readline

pre = [0] * 10000001
for i in range(1, 10000001): # kind of like a sieve
    if pre[i]: # already processed
        continue
    pre[i], j = i, 1
    while i * j * j <= 10000001: # stores the leftover part
        pre[i * j * j] = i
        j += 1

for _ in range(int(input())):
    n, k = map(int, input().split())
    values, segment, ans = [int(i) for i in input().split()], set(), 1
    for value in values: # greedy solution works
        if pre[value] in segment:
            ans += 1
            segment = set()
        segment.add(pre[value])
    print(ans)
