import math, sys

input = sys.stdin.readline

def lcm(x, y):
    return x * y // math.gcd(x, y)

for _ in range(int(input())):
    n = int(input())
    ans, last = n, 1
    for i in range(50):
        last = lcm(last, i + 1)
        ans += n // last
    print(ans % (10 ** 9 + 7))