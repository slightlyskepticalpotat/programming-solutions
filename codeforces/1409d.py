import sys

input = sys.stdin.readline

def sum_of(x):
    ans = 0
    while x:
        ans, x = ans + x % 10, x // 10
    return ans

for _ in range(int(input())):
    n, s = map(int, input().split())
    if sum_of(n) <= s:
        print(0)
    else: # change each number
        ans, level = 0, 1
        for i in range(18):
            d = (n // level) % 10
            n += level * ((10 - d) % 10)
            ans += level * ((10 - d) % 10)
            if sum_of(n) <= s:
                break
            level *= 10
        print(ans)
