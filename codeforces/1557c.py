import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    m, ans = 10 ** 9 + 7, 1
    if n % 2:
        ans = pow(pow(2, n - 1, m) + 1, k, m) # binomial theorem, we can make some even indices 1 or all of them 1 for each bit
    else:
        for i in range(k):
            ans = pow(pow(2, i, m), n, m) + (pow(2, n - 1, m) - 1) * ans
            ans %= m # binomial theorem, we can make some even indices 1 or all of them 1 (and then we can choose any subset of indicies to have 1 in the ith bit) for each bit
    print(ans)