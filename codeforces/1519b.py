import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if n * m - 1 == k:
        print("YES")
    else:
        print("NO")
