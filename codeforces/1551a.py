import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n % 3 == 0:
        print(n // 3, n // 3)
    elif n % 3 == 1:
        print(n // 3 + 1, n // 3)
    elif n % 3 == 2:
        print(n // 3, n // 3 + 1)