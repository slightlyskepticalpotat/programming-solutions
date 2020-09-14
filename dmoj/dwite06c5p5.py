import math, gc

def prime_sieve(x):
    sieve, primes = [True] * x, []
    sieve[0] = False
    sieve[1] = False
    for i in range(2, math.ceil(math.sqrt(x))):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    for i in range(len(sieve)):
        if sieve[i] and palin(i):
            primes.append(i)
    return primes

def palin(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

primes = prime_sieve(1000000)

for i in range(5):
    l, u = map(int, input().split())
    count = 0
    for prime in primes:
        if l <= prime <= u:
            count += 1
    print(count)