import sys

input = sys.stdin.readline

n, s = map(int, input().split())

if s >= 2 * n:
    vals = [2 for i in range(n)]
    s -= 2 * n
    vals[-1] += s
    print("YES")
    print(*vals)
    print(1)
else:
    print("NO")