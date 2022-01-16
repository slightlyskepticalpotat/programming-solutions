import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(pow(a, pow(b, c, 10 ** 9 + 7 - 1), 10 ** 9 + 7))
