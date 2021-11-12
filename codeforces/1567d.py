import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, n = map(int, input().split())
    ans, x = [], 10 ** math.floor(math.log10(s))
    for i in range(n - 1):
        while s - x < n - (i + 1): # positive ints
            x //= 10
        ans, s = ans + [x], s - x
    print(*ans, s)