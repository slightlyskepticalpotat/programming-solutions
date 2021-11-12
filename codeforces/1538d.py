import sys

input = sys.stdin.readline

n, x = map(int, input().split())
d, curr_d, i, j, ans, loc = [int(i) for i in input().split()] * 2, 0, 0, 0, 0, 0
while i < n: # start at
    while curr_d < x:
        loc += (d[j] * (d[j] + 1)) // 2
        curr_d, j = curr_d + d[j], j + 1
    ans = max(ans, loc - ((curr_d - x) * (curr_d - x + 1)) // 2) # subtract start
    loc -= (d[i] * (d[i] + 1)) // 2
    curr_d, i = curr_d - d[i], i + 1
print(ans)