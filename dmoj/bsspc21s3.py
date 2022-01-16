import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a, best = [int(i) for i in input().split()], [float("inf") for i in range(k)] # best[i] is the minimum that we can subtract
best[0], psa, tot = 0, [a[0]], 0
for i in range(1, n):
    psa.append(psa[-1] + a[i])

for i in range(1, n + 1):
    tot = max(tot, psa[i - 1] - best[i % k])
    best[i % k] = min(best[i % k], psa[i - 1])
print(tot)