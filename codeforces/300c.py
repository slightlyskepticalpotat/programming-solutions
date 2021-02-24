def check(x): # check if it only has digits a and b
    while x:
        if x % 10 != a and x % 10 != b:
            return False
        x //= 10
    return True

a, b, n = map(int, input().split())
factorial, ans = [1], 0
for i in range(1, n + 1):
    factorial.append((factorial[-1] * i) % 1000000007)
for i in range(n + 1): # number is something like aaaaaaaaabbb
    if check(a * i + b * (n - i)):
        ans += (factorial[n] * pow(factorial[i] * factorial[n - i], 1000000005, 1000000007))
        ans %= 1000000007
print(ans % 1000000007)
