;import heapq, sys

input = sys.stdin.readline

n, vals, drunk, curr = int(input()), [int(i) for i in input().split()], [], 0
for i in vals:
    curr += i # push to heap regardless
    heapq.heappush(drunk, i)
    if curr < 0: # remove most negative
        curr -= heapq.heappop(drunk)
print(len(drunk))
