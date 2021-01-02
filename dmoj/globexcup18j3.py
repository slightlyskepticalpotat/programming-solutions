import random, sys

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

def sum_of_digits(x):
    return sum([int(i) for i in str(x)])

input = sys.stdin.readline

good = 0
for i in range(int(input())):
    check = int(input())
    if is_prime(check) and is_prime(sum_of_digits(check)):
        good += 1
print(good)