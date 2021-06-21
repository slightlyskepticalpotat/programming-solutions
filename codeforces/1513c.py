import sys

input = sys.stdin.readline

dp = [2] * 9 + [3] + [0] * 199991
for i in range(10, 200001): # len after applying i times to 10
    dp[i] = (dp[i - 9] + dp[i - 10]) % (10 ** 9 + 7)
for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    while n:
        x = n % 10 # last digit
        if m + x < 10:
            ans += 1
        else:
            ans += dp[m + x - 10]
        n //= 10
    print(ans % (10 ** 9 + 7))
