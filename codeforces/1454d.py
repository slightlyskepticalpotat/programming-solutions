import math, statistics

def prime_factors(x):
    factors = []
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        while x % i == 0:
            factors.append(i)
            x /= i
    if x > 1:
        factors.append(int(x))
    return factors

for _ in range(int(input())):
    factors = prime_factors(int(input()))
    k = statistics.multimode(factors)[0]
    n = factors.count(k)
    sequence = [k for i in range(n)]
    sequence[-1] = math.prod(factors) * k // k ** n
    print(n)
    print(*sequence)
