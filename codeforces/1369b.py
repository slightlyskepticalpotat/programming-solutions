import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, ans = int(input()), [int(i) for i in input().strip()], []
    if s == sorted(s):
        ans = [str(i) for i in s]
    else:
        for i in range(n):
            if not s[i]:
                ans.append("0")
            else:
                break
        ans.append("0")
        s = s[::-1]
        for i in range(n):
            if s[i]:
                ans.append("1")
            else:
                break
    print("".join(ans))