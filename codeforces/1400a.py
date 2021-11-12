import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), [i for i in input().strip()]
    print("".join([s[i] for i in range(2 * n - 1) if not i % 2]))
