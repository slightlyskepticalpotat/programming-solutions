import sys

input = sys.stdin.readline

def dp(l, r):
    if l <= r:
        m = (l + r) // 2
        vals[m] = [-(r - l + 1), m] # len, mid
        dp(l, m - 1)
        dp(m + 1, r)

for _ in range(int(input())):
    vals = [0 for i in range(int(input()))]
    ans = [0 for i in range(len(vals))]
    dp(0, len(vals) - 1)

    vals.sort()
    for i in range(len(vals)):
        ans[vals[i][1]] = i + 1
    print(*ans)