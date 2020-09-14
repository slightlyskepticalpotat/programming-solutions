import math

def prime_factors(x):
    factors = []
    for i in range(2, math.ceil(math.sqrt(x)) + 2):
        while x % i == 0:
            factors.append(i)
            x /= i
    if x != 1:
        factors.append(x)
    return factors

for i in range(5):
    n, all_factors, answer = int(input()), [], ""
    for j in range(2, n + 1):
        all_factors += prime_factors(j)
    for k in sorted(set(all_factors)):
        if all_factors.count(k) != 0:
            answer += f"{k}^{all_factors.count(k)} * "
    print(answer[:-2])