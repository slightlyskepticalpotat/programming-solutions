import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], -1
    for i in range(n - 1):
        ans = max(ans, vals[i] * vals[i + 1])
    print(ans)