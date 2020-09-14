import sys
input = sys.stdin.readline

def prime_sieve(x):
    sieve = [0] * (x + 1)
    for i in range(2, x, 2): # even numbers aren't prime
        sieve[i] += 1
    for i in range(3, x, 2): # check odd numbers
        if sieve[i] == 0: # if number is prime
            for j in range(i, x, i): # multiples of the prime numbers
                sieve[j] += 1
    return sieve

sieve = prime_sieve(1000001)

start, stop = int(input()), int(input())
for i in range(start, stop + 1):
  print(sieve[i])