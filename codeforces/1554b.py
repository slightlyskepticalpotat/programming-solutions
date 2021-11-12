import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    vals, ans = [int(i) for i in input().split()], -float("inf")
    for i in range(max(0, n - 2 * k - 1), n):
        for j in range(i + 1, n):
            ans = max(ans, (i + 1) * (j + 1) - k * (vals[i] | vals[j]))
    print(ans)