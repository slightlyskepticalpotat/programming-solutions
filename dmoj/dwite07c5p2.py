def prime_factors(x):
    factors = []
    for i in range(2, x//2 + 1):
        while x % i == 0:
            factors.append(i)
            x/=i
    return len(factors)

for i in range(5):
    print(prime_factors(int(input())))