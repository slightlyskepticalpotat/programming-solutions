import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, ans = input().strip(), ""
    new = s + "a"
    if new != new[::-1]:
        ans = new
    new = "a" + s
    if new != new[::-1]:
        ans = new
    if ans:
        print("YES")
        print(ans)
    else:
        print("NO")
