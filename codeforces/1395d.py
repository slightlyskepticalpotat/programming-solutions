import sys

input = sys.stdin.readline

n, d, m = map(int, input().split())
vals = sorted([int(i) for i in input().split()], reverse = True)
over, under, over_psa, under_psa, ans = [i for i in vals if i > m], [i for i in vals if i <= m], [0], [0], 0
for i in range(len(over)):
    over_psa.append(over_psa[i] + over[i])
for i in range(n - len(over)): # prevent indexerror
    over_psa.append(over_psa[-1])
for i in range(len(under)):
    under_psa.append(under_psa[i] + under[i])
for i in range(n - len(under)): # prevent indexerror
    under_psa.append(under_psa[-1])
print(max([over_psa[i] + under_psa[n - max(((i - 1) * (d + 1) + 1), 0)] if (i - 1) * (d + 1) + 1 <= n else 0 for i in range(len(over) + 1)])) # iterate by times muted
