import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ratings = [int(i) for i in input().strip().split()]
psa = [0, ratings[0]]
for i in range(1, n):
    psa.append(psa[i] + ratings[i])

for i in range(q):
    a, b = map(int, input().split())
    print(psa[-1] - (psa[b] - psa[a - 1])) # total - skipped episodes