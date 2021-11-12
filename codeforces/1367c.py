import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    blocks = ("0" * k + input().strip() + "0" * k).split("1")
    print(sum(max(0, len(block) - k) // (k + 1) for block in blocks))