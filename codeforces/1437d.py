import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    s, c = [0 for i in range(n)], 0
    for i in range(1, n):
        c += vals[i - 1] > vals[i]
        s[i] = s[c] + 1
    print(s[n - 1])