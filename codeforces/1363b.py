import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, ans = input().strip(), []
    for i in range(len(s) + 1):
        ans.append(s[i:].count("0") + s[:i].count("1")) # change these
        ans.append(s[i:].count("1") + s[:i].count("0")) # change these
    print(min(ans))