import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, z = map(int, input().split())
    vals, ans = [int(i) for i in input().split()], 0
    for i in range(z + 1):
        if k - 2 * i >= 0:
            best = 0
            for j in range(k - 2 * i + 1):
                if j < n - 1:
                    best = max(best, vals[j] + vals[j + 1])
            ans = max(ans, sum(vals[:k - 2 * i + 1]) + i * best) # moving right and moving left
    print(ans)
