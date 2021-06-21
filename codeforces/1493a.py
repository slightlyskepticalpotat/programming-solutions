import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = []
    for i in range(k + 1, n + 1): # k + 1 to n
        ans.append(i)
    for i in range((k + 1) // 2, k): # 0 to k / 2
        ans.append(i)
    print(len(ans))
    print(*ans)
