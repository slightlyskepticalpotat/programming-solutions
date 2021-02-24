import math

def prime_factors(x):
    factors = set()
    for i in range(2, 10 ** 5 + 1):
        while not x % i:
            factors.add(i)
            x /= i
    if x != 1:
        factors.add(x)
    return factors

for _ in range(int(input())):
    p, q = map(int, input().split())
    factors, can = prime_factors(q), []
    for factor in factors:
        res = p
        while not res % q:
            res //= factor
        can.append(res)
    print(int(max(can)))
