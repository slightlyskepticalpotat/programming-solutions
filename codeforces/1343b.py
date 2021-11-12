import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, ans = int(input()) // 2, []
    if n % 2:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            ans.append((i + 1) * 2)
        for i in range(n - 1):
            ans.append(i * 2 + 1)
        ans.append(sum(ans[:n]) * 2 - sum(ans))
        print(*ans)