import sys

input = sys.stdin.readline

n = [int(i) for i in input().strip()]
if 0 not in n or sum(n) % 3 != 0:
    print("-1")
else:
    n.sort(reverse = True)
    print("".join([str(i) for i in n[:-1]]) + "0")