# gcd(a, b) = gcd(a-b, b)

import functools, math, sys

input = sys.stdin.readline

n, m = map(int, input().split())
a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
try:
    modified_gcd = functools.reduce(math.gcd, [a[i] - a[0] for i in range(1, n)])
except:
    modified_gcd = 0
print(*[math.gcd(a[0] + b[i], modified_gcd) for i in range(m)])
