import sys

input = sys.stdin.readline

n, vals = int(input()), [int(i) for i in input().split()]
vals = [[vals[i], i + 1] for i in range(len(vals))]
vals = list(sorted(vals, key = lambda x: x[0]))
left, right, m = vals[:n], vals[n:], 0
for i in range(n):
    if left[i][0] != right[i][0]:
        m += 1
print(m)
for i in range(n):
    print(left[i][1], right[i][1])