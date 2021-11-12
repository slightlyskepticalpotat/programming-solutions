import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a = int(input()), [int(i) for i in input().split()]
    b = [a[0]]
    for i in range(1, n):
        b.append(max(b[-1], a[i]))
    print(max([math.floor(math.log2(b[i] - a[i])) + 1 for i in range(n) if b[i] - a[i]] + [0]))
