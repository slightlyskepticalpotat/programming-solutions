import math, sys

input = sys.stdin.readline

def num_factors(x):
    n = 0
    while not x % 2:
        x //= 2
        n += 1
    i = 3
    while x != 1 and i < 31622:
        if x % i == 0:
            n += 1
            x /= i
        else:
            i += 2
    if x != 1:
        n += 1
    return n

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    most, least, limit = num_factors(a) + num_factors(b), 2, -1
    if a == b:
        least = 0
        limit = 1
    elif 0 in [a % b, b % a]:
        least = 1
    if least <= k <= most and k != limit:
        print("YES")
    else:
        print("NO")
