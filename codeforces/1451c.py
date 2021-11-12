import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a, b, af, bf, flag = input().strip(), input().strip(), {i: 0 for i in "abcdefghijklmnopqrstuvwxyz{"}, {i: 0 for i in "abcdefghijklmnopqrstuvwxyz{"}, True
    for i in range(n):
        af[a[i]] += 1
        bf[b[i]] += 1
    for i in "abcdefghijklmnopqrstuvwxyz":
        if bf[i] > af[i] or (af[i] - bf[i]) % k:
            flag = False
        af[i] -= bf[i]
        af[chr(ord(i) + 1)] += af[i]
    if flag:
        print("Yes")
    else:
        print("No")
