import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], []
    if set(vals) == {0}:
        ans = [i + 1 for i in range(n + 1)]
    else:
        for i in range(1, n + 1):
            if vals[i - 1] == 0:
                ans.append(i)
            else:
                ans.extend([n + 1, i])
                break
        for i in range(i, n):
            ans.append(i + 1)
    print(*ans)