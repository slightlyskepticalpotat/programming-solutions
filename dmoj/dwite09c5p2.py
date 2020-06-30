# https://dmoj.ca/problem/dwite09c5p2
from random import randint

def is_prime(n):
    iterations = 2
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

for i in range(5):
    number = int(input())
    number_top = number
    number_bot = number
    mid_top = 0
    mid_bot = 0
    prime_top = 0
    prime_bot = 0
    while True:
        number_top+=1
        if is_prime(number_top) and mid_top == 0:
            mid_top = 1
        elif is_prime(number_top) and mid_top == 1:
            prime_top = number_top
            break
    while True:
        number_bot-=1
        if is_prime(number_bot) and mid_bot == 0:
            mid_bot = 1
        elif is_prime(number_bot) and mid_bot == 1:
            prime_bot = number_bot
            break
    if abs(prime_top - number) <= abs(prime_bot - number):
        print(prime_top)
    else:
        print(prime_bot)