import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    one, two, three, ans = -1, -1, -1, []
    for i in range(len(s)):
        if s[i] == "1":
            one = i
        elif s[i] == "2":
            two = i
        else:
            three = i
        if min(one, two, three) != -1:
            ans.append(max(one, two, three) - min(one, two, three) + 1)
    if ans:
        print(min(ans))
    else:
        print(0)