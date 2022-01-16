import sys

input = sys.stdin.readline

n, h, p = map(int, input().split())
a, psa = list(sorted([int(i) for i in input().split()])), [0]
for i in range(n):
    psa.append(psa[i] + a[i])
best = psa[-1] * p
for i in range(n):
    best = min(best, a[i] * h + max(psa[-1] - psa[i + 1] - (a[i] * (n - i - 1)), 0) * p)
print(best)