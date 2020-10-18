import sys

input = sys.stdin.readline

l, r, sum, min = 0, 0, 0, float("inf")
n, m = map(int, input().split())
damage = [int(i) for i in input().split()]

while r <= n:
    if sum < m:
        try:
            sum += damage[r]
        except:
            sum += damage[r - 1]
        r += 1
    elif sum >= m:
        sum -= damage[l]
        l += 1
        if (r - l + 1) < min:
            min = (r - l + 1)

if min != float("inf"):
    print(min)
else:
    print(-1)