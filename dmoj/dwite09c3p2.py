import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def calc(x):
    if x == 0:
        return (0, 1)
    else:
        k, kplusone = calc(int(x // 2))
        twok = k * (2 * kplusone - k)
        twokplusone = k**2 + kplusone**2
        if x % 2 == 0:
            return (twok, twokplusone)
        else:
            return (twokplusone, twok + twokplusone)

for _ in range(5):
    n = int(input())
    for i in range(0, n**2+1):
        if calc(i)[0] >= n:
            if abs(calc(i-1)[0] - n) >= abs(calc(i)[0] - n):
                print(calc(i)[0])
                break
            else:
                print(calc(i-1)[0])
                break