import sys

input = sys.stdin.readline

n, k = map(int, input().split())
m, c, ans = sorted([int(i) for i in input().split()], reverse=True), [int(i) for i in input().split()], 0
for i in range(n):
    ans = max(ans, (i + c[m[i] - 1]) // c[m[i] - 1])
cases = [[] for i in range(ans)]
for i in range(n):
    cases[i % ans].append(m[i])
print(ans)
for i in range(ans):
    print(len(cases[i]), *cases[i])