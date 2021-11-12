import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    if min(a, b) >= m and (n + m) <= (a + b):
        print("YES")
    else:
        print("NO")
