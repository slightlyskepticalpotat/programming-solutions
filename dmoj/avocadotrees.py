import sys

input = sys.stdin.readline

n, q, h = map(int, input().split())
trees, psa, best = [0 for _ in range(n)], [0], 0

for i in range(n):
	ai, bi = map(int, input().split())
	if ai <= h:
		trees[i] = bi

for i in range(n):
	psa.append(psa[i] + trees[i])
	
for _ in range(q):
	l, r = map(int, input().split())
	best = max(best, psa[r] - psa[l - 1])

print(best)