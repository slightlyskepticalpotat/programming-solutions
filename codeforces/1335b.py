import string, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    letters = string.ascii_lowercase[:b] * n
    print(letters[:n])