import math
cases = int(input())

def primefactors(x):
    prime_factors = []
    
    while x % 2 == 0:
        prime_factors.append(2)
        x = x/2
    for i in range(3, int(math.sqrt(x))+1,2):
        while x % i == 0:
            prime_factors.append(int(i))
            x = x/i
    if x > 2:
        prime_factors.append(int(x))
        
    prime_factors.sort()
    prime_factors_str = ' '.join(str(j) for j in prime_factors)
    return prime_factors_str
    
for i in range(0,cases):
    number = int(input())
    print(primefactors(number))