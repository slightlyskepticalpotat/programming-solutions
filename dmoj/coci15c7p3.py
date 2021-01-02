import sys

input = sys.stdin.readline

k = int(input())
raw = [int(i) for i in input().split()]
pxa, k = [0], k + 1 # prefix xor array
for i in range(1, k):
    pxa.append(pxa[i - 1] ^ raw[i - 1])
pxa += pxa

for i in range(int(input())):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    l, r = l % k, l % k + (r - l + 1) % k
    print(pxa[l] ^ pxa[r])