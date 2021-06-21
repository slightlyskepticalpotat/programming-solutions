import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, seen, sus = int(input()), input().strip(), set(), False
    for i in range(n):
        if s[i] in seen and s[i - 1] != s[i]:
            sus = True
        seen.add(s[i])
    if sus:
        print("NO")
    else:
        print("YES")
