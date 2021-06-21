import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    low, cnt, ans = min(values), values.count(min(values)), float("inf")
    for i in range(n):
        if low & values[i] != low:
            ans = 0
    ans = min(ans, pow(cnt * (cnt - 1) * math.factorial(n - 2), 1, 10 ** 9 + 7))
    print(ans)
