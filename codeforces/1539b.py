import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s, psa = [ord(char) - 96 for char in input().strip()], [0]
for i in range(n):
    psa.append(s[i] + psa[i])

for _ in range(q):
    l, r = map(int, input().split())
    print(psa[r] - psa[l - 1])
