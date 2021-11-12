import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], 0
    for i in range(n - 1):
        for j in range(vals[i] - i - 2, n, vals[i]):
            ans += int(i < j and vals[i] * vals[j] == (i + j + 2))
    print(ans)