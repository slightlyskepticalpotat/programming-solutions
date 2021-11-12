import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, v, ans = int(input()), input().strip(), 0, 0
    for c in s:
        if c == "(":
            v += 1
        else:
            v -= 1
        ans = min(ans, v)
    print(abs(ans))
