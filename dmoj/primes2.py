import math

def simple_prime_sieve(x):
    sieve, primes = [True] * x, []
    sieve[0] = False
    sieve[1] = False
    for i in range(2, x):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, x, i):
                sieve[j] = False
    return primes

def primes_in_range(x, y):
    primes = simple_prime_sieve(math.floor(math.sqrt(y)) + 2)
    sieve, new_primes = [True] * (y - x + 2), []
    for i in range(len(primes)): # minimum number in range multiple of prime
        limit = math.floor(x / primes[i]) * primes[i]
        if limit < x: # we underestimated
            limit += primes[i]
        if limit == primes[i]: # we underestimated
            limit += primes[i]
        for j in range(limit, y + 1, primes[i]):
            sieve[j - x] = False
    for i in range(max(2, x), y + 1): # remove 1
        if sieve[i - x]:
            all_primes.append(i)
    return 0

n, m = map(int, input().split())
all_primes = []
primes_in_range(max(2, n), math.floor(n + 1 / 4 * (m - n)))
primes_in_range(math.floor(n + (1 / 4) * (m - n)) + 1, math.floor(n + (2 / 4) * (m - n)))
primes_in_range(math.floor(n + (2 / 4) * (m - n)) + 1, math.floor(n + (3 / 4) * (m - n)))
primes_in_range(math.floor(n + (3 / 4) * (m - n)) + 1, m)
for prime in all_primes:
    print(prime)