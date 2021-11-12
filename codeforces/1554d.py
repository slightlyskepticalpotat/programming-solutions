import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print("z")
    elif n % 2:
        print("a" * (n // 2) + "yz" + "a" * (n // 2 - 1))
    else:
        print("a" * (n // 2) + "z" + "a" * (n // 2 - 1))