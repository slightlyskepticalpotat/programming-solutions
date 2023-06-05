import math, sys

input = sys.stdin.readline

def prime_factors(x):
    factors = []
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        while x % i == 0:
            factors.append(i)
            x /= i
    if x > 1:
        factors.append(int(x))
    return factors

candies, final, j = [i - 1 for i in prime_factors(int(input()) + 1)], [], 1 # include empty set
if sum(candies) > 10 ** 5:
    print("Sad Chris")
else:
    for i in range(len(candies)):
        final.extend([i + 1] * candies[i])
    print(len(final))
    print(*final)
