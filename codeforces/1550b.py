import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input().strip()
    groups = [[s[0]]]
    for i in range(1, n):
        if s[i] == groups[-1][0]:
            groups[-1].append(s[i])
        else:
            groups.append([s[i]])
    print(a * n + max(b * (len(groups) // 2 + 1), b * n))
