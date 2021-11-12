import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    vals, psa = sorted([int(i) for i in input().split()])[::-1], [0]
    for i in range(n):
        psa.append(psa[i] + vals[i])
    for i in range(n + 1):
        if psa[i] >= i * x:
            ans = i
    print(ans)