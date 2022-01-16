import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    g, ans = math.gcd(a, b), 0
    a, b = a // g, b // g
    new_b = b
    while not new_b % 2:
        new_b //= 2
    while not new_b % 5:
        new_b //= 5
    if new_b != 1: # repeating
        print(-1)
    else:
        while a % b:
            a, ans = a % b, ans + 1
            a *= 10
        print(ans)