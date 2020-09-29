import math

def factors(x):
    factors = set()
    for i in range(1, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            factors.add(x)
            factors.add(x // i)
    factors.remove(x)
    return factors

n = int(input())
try:
    print(n - max(factors(n))) 
except: # prime
    print(n - 1)