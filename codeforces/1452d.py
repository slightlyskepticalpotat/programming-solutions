def calc(x):
    if x == 0:
        return (0, 1)
    else:
        k, kplusone = calc(int(x // 2))
        twok = k * pow((2 * kplusone - k + r), 1, r)
        twokplusone = pow((pow(k**2, 1, r) + pow(kplusone**2, 1, r)), 1, r)
        if x % 2 == 0:
            return (twok, twokplusone)
        else:
            return (twokplusone, pow((twok + twokplusone), 1, r))

n, r = int(input()), 998244353
top = calc(n)[0] % r # fib
bottom = pow(2 ** n, -1, r) # modinv
print((top * bottom) % r) # fib(n) / 2 ** n == x / y
