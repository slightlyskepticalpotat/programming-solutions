import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    values = [int(i) for i in input().split()]
    psa, best = [values[0]], 0
    for i in range(1, n):
        psa.append(psa[i - 1] + values[i])
    for i in range(1, n):
        best = max(best, (100 * values[i] - k * psa[i - 1] + k - 1) // k)
    print(best)
