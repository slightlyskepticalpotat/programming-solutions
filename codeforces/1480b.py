import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    attack, health = [int(i) for i in input().split()], [int(i) for i in input().split()]
    combined = list(sorted([[attack[i], health[i]] for i in range(n)], key = lambda x: x[0]))
    for i in range(n - 1):
        b -= combined[i][0] * math.ceil(combined[i][1] / a)
    if combined[-1][0] * (math.ceil(combined[-1][1] / a) - 1) < b:
        print("YES")
    else:
        print("NO")
