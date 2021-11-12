import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip()
    if s == s[::-1]:
        if not s.count("0") % 2 or s.count("0") == 1:
            print("BOB")
        else:
            print("ALICE")
    else:
        if n % 2 and s.count("0") == 2 and s[n // 2] == "0":
            print("DRAW")
        else:
            print("ALICE")
