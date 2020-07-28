import sys
from random import randint

input = sys.stdin.readline

def is_prime(n):
    iterations = 4
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    s, d = 0, n-1
    while pow(d, 1, 2) == 0:
        s, d = s+1, d//2
    for i in range(iterations):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1:
            continue
        for r in range(1, s):
            x = pow(x*x, 1, n)
            if x == 1:
                return False
            if x == n-1:
                break
        else:
            return False
    return True

for i in range(int(input())):
    primes = 0
    start, stop = map(int, input().split())
    for j in range(start, stop):
        if is_prime(j):
            primes+=1
    print(primes)