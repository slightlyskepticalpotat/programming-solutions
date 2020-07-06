# https://www.facebook.com/notes/facebook-hacker-cup/hacker-cup-2015-round-1-solutions/1047761065239794/

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

sieve = prime_sieve(10000008)

for i in range(1, int(input()) + 1):
    a, b, k = map(int, input().split())
    answer = 0
    for j in range(a, b + 1):
        if sieve[j] == k:
            answer+=1
    print("Case #{case}: {answer}".format(case=i, answer=answer))