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

def iteration(x):
    if is_prime(x):
        x *= 11
    elif math.sqrt(x) == math.floor(math.sqrt(x)):
        x += int(str(x)[::-1])
    elif str(x) == str(x)[::-1]:
        x = int(str(x) + "4")
    elif str(x)[0] == "2":
        x = int("5" + str(x))
    elif "7" in str(x):
        x = int(str(x)[:-1])
    elif x // 6 == x / 6:
        x = int(str(x)[1:])
    elif len(str(x)) % 2 == 0:
        y = len(str(x))
        x = int(str(x)[:y // 2] + "1" + str(x)[y // 2:])
    elif len(str(x)) % 2 == 1:
        x += 231
    return x

for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(b):
        a = iteration(a)
    print(a)