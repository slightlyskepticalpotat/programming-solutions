import sys

input = sys.stdin.buffer.readline # faster than sys.stdin.readline

def sieve_min_prime(x):
    sieve = [0] * x
    for i in range(2, x):
        if not sieve[i]:
            sieve[i] = i
            for j in range(i * i, x, i):
                if not sieve[j]:
                    sieve[j] = i
    return sieve

n, vals = int(input()), [int(i) for i in input().split()]
sieve, d1, d2 = sieve_min_prime(10 ** 7 + 1), [], []
for i in range(n):
    j = vals[i]
    while not j % sieve[vals[i]]:
        j //= sieve[vals[i]]
    if j == 1: # more than one prime factor
        d1.append(-1)
        d2.append(-1)
    else:
        d1.append(j)
        d2.append(sieve[vals[i]])
print(*d1)
print(*d2)