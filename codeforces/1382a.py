import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
    a, b, ans = set(a), set(b), 0
    for i in a:
        if i in b:
            ans = i
    if ans:
        print("YES")
        print(1, ans)
    else:
        print("NO")
