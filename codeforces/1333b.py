import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b, pos, neg, ans = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()], False, False, True
    for i in range(n):
        ans &= (a[i] < b[i] and pos) or (a[i] > b[i] and neg) or (a[i] == b[i])
        pos |= a[i] == 1
        neg |= a[i] == -1
    if ans:
        print("YES")
    else:
        print("NO")