import random, math

def prime_sieve(x):
    sieve = [True] * x
    sieve[0] = False
    sieve[1] = False
    for i in range(2, math.ceil(math.sqrt(x))):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    return sieve

n, values = int(input()), [int(i) for i in input().split()]
primes = prime_sieve(1000001)
for value in values:
    can = math.sqrt(value)
    if can == math.floor(can) and primes[math.floor(can)]:
        print("YES")
    else:
        print("NO")
