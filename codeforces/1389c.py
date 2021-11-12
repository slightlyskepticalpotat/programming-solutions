import sys

input = sys.stdin.readline

for _ in range(int(input())): # xxxxx or xyxy
    s, ans = [int(i) for i in input().strip()], 0
    for i in range(10):
        for j in range(10):
            target, loc = [i, j], 0
            for k in range(len(s)):
                loc += int(s[k] == target[loc % 2])
            if i != j:
                loc = (loc // 2) * 2
            ans = max(ans, loc)
    print(len(s) - ans)
