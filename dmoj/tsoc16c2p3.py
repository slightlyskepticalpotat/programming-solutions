import math, random

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
        x = pow(random.randint(2, n-1), d, n)
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

a, b, c, d = map(int, input().split())
total = 0
for i in range(a, b + 1):
    if is_prime(i):
        total += (((d // i * i) - (math.ceil(c / i) * i)) // i + 1) * ((d // i * i) + (math.ceil(c / i) * i)) * 1 / 2 # smallest and largest multiples in range
print(int(total) % 2016420)