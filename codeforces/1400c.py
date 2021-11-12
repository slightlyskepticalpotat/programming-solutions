import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, x = [int(i) for i in input().strip()], int(input())
    w, n, ans = [1 for i in range(len(s))], len(s), True
    for i in range(n):
        if not s[i]:
            if 0 <= i - x < n:
                w[i - x] = 0
            if 0 <= i + x < n:
                w[i + x] = 0
    for i in range(n):
        check = set()
        if 0 <= i - x < n:
            check.add(w[i - x])
        if 0 <= i + x < n:
            check.add(w[i + x])
        if s[i] and 1 not in check:
            ans = False
    if ans:
        print("".join([str(i) for i in w]))
    else:
        print(-1)
