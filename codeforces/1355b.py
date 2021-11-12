import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, last, ans = int(input()), sorted([int(i) for i in input().split()]), 0, 0
    for i in range(n):
        if i - last + 1 >= vals[i]:
            last, ans = i + 1, ans + 1
    print(ans)