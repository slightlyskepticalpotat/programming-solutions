import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], []
    for i in range(n):
        if i == 0 or i == n - 1 or vals[i - 1] < vals[i] > vals[i + 1] or vals[i - 1] > vals[i] < vals[i + 1]:
            ans.append(vals[i])
    print(len(ans))
    print(*ans)