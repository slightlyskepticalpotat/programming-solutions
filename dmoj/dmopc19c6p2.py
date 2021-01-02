# legendre's formula

import math

def prime_factors(x):
    factors = []
    for i in range(2, math.ceil(math.sqrt(x))):
        while x % i == 0:
            factors.append(i)
            x/=i
    if x > 1:
        factors.append(x)
    return factors

a, b = map(int, input().split())
factors, best = prime_factors(a), float("inf")
for factor in set(factors):
    local, i = 0, 1
    while b // (factor ** i):
        local +=  b // (factor ** i)
        i += 1
    local //= factors.count(factor)
    best = min(best, local)
print(int(best))