import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, e, g, ans = int(input()), [int(i) for i in input().strip()], [int(i) for i in input().strip()], 0
    for i in range(n):
        if g[i]:
            if i != 0 and e[i - 1] == 1:
                ans, e[i - 1] = ans + 1, -1
            elif e[i] == 0:
                ans, e[i] = ans + 1, -1
            elif i != n - 1 and e[i + 1] == 1:
                ans, e[i + 1] = ans + 1, -1
    print(ans)