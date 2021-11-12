import math, random

def is_prime(n):
    iterations = 8
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

for _ in range(int(input())):
    d, f, s = int(input()), -1, -1
    i = d + 1
    while True:
        if is_prime(i):
            f = i
            break
        i += 1
    i = f + d
    while True:
        if is_prime(i):
            s = i
            break
        i += 1
    print(min(f * s, f * f * f))
