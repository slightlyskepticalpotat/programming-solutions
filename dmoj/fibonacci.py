import sys
n = int(sys.stdin.readline())
n = pow(n, 1, 2000000016)
sys.setrecursionlimit(10000)
r = 1000000007

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
print(pow((calc(n)[0]), 1, r))