import sys

input = sys.stdin.readline

n = int(input())
if not n % 2 and not n % 3 and str(n)[-1] != "2":
    print("not a memer")
else:
    print("memer")
