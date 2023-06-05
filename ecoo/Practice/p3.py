import sys

input = sys.stdin.readline

n, c, q = map(int, input().split())
cookies = [c for _ in range(n)]
for _ in range(q):
    ni = int(input())
    for i in range(n):
        if not (i + 1) % ni:
            cookies[i] = max(0, cookies[i] - 1)
print(sum(cookies))
