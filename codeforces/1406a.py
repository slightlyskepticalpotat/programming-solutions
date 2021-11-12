import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, cnt, a, b = int(input()), [int(i) for i in input().split()], {i: 0 for i in range(101)}, float("inf"), float("inf")
    for value in values:
        cnt[value] += 1
    for i in range(101):
        if cnt[i] == 0:
            a = min(a, i)
        if cnt[i] <= 1:
            b = min(b, i)
    print(a + b)
