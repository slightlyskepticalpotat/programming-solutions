import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, i = int(input()), 4
    while i - 1 <= n:
        if not n % (i - 1):
            print(n // (i - 1))
            break
        i *= 2