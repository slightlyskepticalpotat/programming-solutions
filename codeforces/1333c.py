import sys

input = sys.stdin.readline

n, vals, current, best, ans, last = int(input()), [int(i) for i in input().split()], 0, 0, 0, {0: 0}
for i in range(n):
    current += vals[i]
    if current in last:
        best = min(best, i - last[current] - 1)
    best += 1
    ans, last[current] = ans + best, i + 1
print(ans)