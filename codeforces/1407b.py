import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b, gcd_prefix = int(input()), [int(i) for i in input().split()], [], 0
    while a:
        cache = max(a, key = lambda x: math.gcd(x, gcd_prefix))
        gcd_prefix = math.gcd(cache, gcd_prefix)
        b.append(cache)
        a.remove(cache)
    print(*b)
