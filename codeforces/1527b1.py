import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip().count("0")
    if not s % 2 or s == 1:
        print("BOB")
    else:
        print("ALICE")
