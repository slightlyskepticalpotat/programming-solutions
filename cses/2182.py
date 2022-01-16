import sys

input = sys.stdin.readline

primes, powers, prod, prod_alt, total, number, mod = [], [], 1, 1, 1, 1, 10 ** 9 + 7
for _ in range(int(input())):
    x, k = map(int, input().split())
    primes.append(x)
    powers.append(k)
for i in range(len(primes)):
    prod = (prod * (powers[i] + 1)) % mod
    total = total * (((pow(primes[i], powers[i] + 1, mod) - 1) % mod) * pow(primes[i] - 1, mod - 2, mod)) % mod
    number = ((pow(number, powers[i] + 1, mod) * pow(pow(primes[i], powers[i] * (powers[i] + 1) // 2, mod), prod_alt, mod))) % mod
    prod_alt = (prod_alt * (powers[i] + 1)) % (mod - 1)
print(prod, total, number)
