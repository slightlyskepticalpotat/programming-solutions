import math, sys

input = sys.stdin.readline

def factors(x):
    factors = []
    for i in range(1, math.floor(math.sqrt(x)) + 1):
        if not x % i:
            factors.append(i)
            factors.append(x // i)
    factors.remove(x)
    return factors

for _ in range(int(input())):
    n = int(input())
    a = max(factors(n))
    b = n - a
    print(a, b)
