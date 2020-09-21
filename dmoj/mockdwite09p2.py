import math

def simple_prime_sieve(x):
    sieve = [True] * x
    sieve[0] = False
    sieve[1] = False
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    return sieve

sieve = simple_prime_sieve(1000001)

for _ in range(5):
    digits = []
    a, b = input().strip().split("_")
    a = "0" + a
    for i in range(10):
        if sieve[int(a + str(i) + b)]: # also check for leading zeros
            digits.append(i)
    if digits:
        print(*digits)
    else:
        print("Not possible")