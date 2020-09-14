import math, sys

input = sys.stdin.readline

def prime_sieve(x):
    sieve = [True] * x
    sieve[0] = False
    sieve[1] = False
    for i in range(2, math.ceil(math.sqrt(x))):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    return sieve

primes, sieve = [0] * 1000001, prime_sieve(1000001)

for i in range(1000001): # prefix array
    primes[i] = primes[i - 1]
    if sieve[i]:
        primes[i] += 1

for i in range(int(input())):
    a, b = map(int, input().split())
    print(primes[b - 1] - primes[a - 1])