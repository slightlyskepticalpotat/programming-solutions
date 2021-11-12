import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) // 2
    print((n * (n + 1) * (2 * n + 1)) * 8 // 6)