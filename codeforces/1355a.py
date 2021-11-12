import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, k = map(int, input().split())
    for i in range(k - 1):
        digits = [int(j) for j in str(a)]
        l, r = min(digits), max(digits)
        if l == 0:
            break
        a += l * r
    print(a)