import math

def prime_factors(x):
    factors = []
    for i in range(2, math.ceil(math.sqrt(x))):
        while x % i == 0:
            factors.append(i)
            x/=i
    if x > 1:
        factors.append(x)
    return sorted(factors)

for thing in prime_factors(int(input())):
    print(int(thing))