import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    i, ans = 1, False
    while i <= n:
        ans |= not (n - i) % b
        if a == 1:
            break
        i *= a
    if ans:
        print("Yes")
    else:
        print("No")