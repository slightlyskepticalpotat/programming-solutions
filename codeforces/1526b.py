import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if not n % 11 or n - (n % 11) * 111 >= 0:
        print("YES")
    else:
        print("NO")
