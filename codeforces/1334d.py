import sys

input = sys.stdin.readline

for _ in range(int(input())): # n = 4, 1 2 1 3 1 4 | 2 3 2 4 | 3 4 | 1
    n, l, r = map(int, input().split())
    i, ans = 1, []
    while l - 1 > (n - i) * 2:
        l, r, i = l - (n - i) * 2, r - (n - i) * 2, i + 1
    while r > len(ans) and i < n:
        for j in range(i, n):
            ans.append(i)
            ans.append(j + 1)
        i += 1
    ans.append(1)
    print(*ans[l - 1:r])