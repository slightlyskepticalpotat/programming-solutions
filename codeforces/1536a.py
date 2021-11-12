import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a = int(input()), [int(i) for i in input().split()]
    if min(a) < 0 or len(a) != len(set(a)):
        print("NO")
    else:
        print("YES")
        print(101)
        print(*[i for i in range(101)])
