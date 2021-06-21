import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    r = (x - 1) % n
    c = (x - 1) // n
    print(r * m + c + 1)
