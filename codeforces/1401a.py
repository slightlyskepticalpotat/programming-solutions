import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n < k:
        print(k - n)
    else:
        print(int(bool((n + k) % 2)))
