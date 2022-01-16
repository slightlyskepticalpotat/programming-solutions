import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())
g, p = a < b, c < d
if g and p:
    print("Go to the department store")
elif g:
    print("Go to the grocery store")
elif p:
    print("Go to the pharmacy")
else:
    print("Stay home")