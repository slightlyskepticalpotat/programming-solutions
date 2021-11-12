import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    o, ans = [int(i) % 2 for i in input().split()].count(1), False
    for i in range(1, min(o, x) + 1, 2):
        ans |= (n - o) >= (x - i)
    if ans:
        print("Yes")
    else:
        print("No")