import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, t, m, ans = int(input()), input().strip(), [], [], True
    for i in range(n):
        if s[i] == "T":
            t.append(i)
        else:
            m.append(i)
    if len(t) != len(m) * 2:
        ans = False
    else:
        for i in range(len(m)):
            if not t[i] < m[i] or not m[i] < t[i + len(m)]:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")
