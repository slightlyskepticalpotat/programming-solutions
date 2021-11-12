import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    n -= (k - 3)
    if n % 2:
        print(n // 2, n // 2, 1, *[1 for i in range(k - 3)])
    else:
        if n % 4:
            print(n // 2 - 1, n // 2 - 1, 2, *[1 for i in range(k - 3)])
        else:
            print(n // 2, n // 4, n // 4, *[1 for i in range(k - 3)])
