import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7

n, ans = int(input()), 1
for i in range(1, n + 1):
    ans = (ans * i) % MOD
print((ans - (1 << (n - 1))) % MOD)
