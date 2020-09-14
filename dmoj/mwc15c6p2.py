import math, sys

input = sys.stdin.readline

def prime_sieve(x):
    sieve = [True] * (x + 1)
    for i in range(2, math.ceil(math.sqrt(x))):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    return sieve

def biggest(x): # biggest prime lower than x
    while True:
        if sieve[x - 1]:
            return x - 1
        x -= 1

sieve = prime_sieve(10001)
n = int(input())
slices = [int(i) for i in input().split()]

for slice in slices:
    how_to_lose = biggest(slice)
    if how_to_lose < 2:
        print("no can do")
    else:
        print(how_to_lose)