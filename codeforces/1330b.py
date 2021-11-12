import sys

input = sys.stdin.readline

def perm(x):
    check = [i + 1 for i in range(len(x))]
    return check == sorted(x)

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], set()
    maximum = max(vals)
    left, right = vals[:maximum], vals[maximum:]
    if perm(left) and perm(right):
        ans.add((maximum, n - maximum))
    left, right = vals[:n - maximum], vals[n - maximum:]
    if perm(left) and perm(right):
        ans.add((n - maximum, maximum))
    print(len(ans))
    for i in ans:
        print(*i)