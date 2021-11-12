import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a, b, pre, ans = input().strip() + "0", input().strip() + "0", [0, 0], True
    for i in range(n):
        pre[int(b[i])] += 1
        if (a[i] == b[i]) != (a[i + 1] == b[i + 1]):
            if pre[0] != pre[1]:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")
