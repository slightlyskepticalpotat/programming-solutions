import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()]
    type_0, type_1 = [a[i] for i in range(n) if not b[i]], [a[i] for i in range(n) if b[i]]
    if type_0 and type_1 or (a == sorted(a)):
        print("Yes")
    else:
        print("No")