import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int, input().split())
    ans = 0
    while max(l, r) != 0:
        ans += r - l
        l //= 10
        r //= 10
    print(ans)
