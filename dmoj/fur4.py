import sys

input = sys.stdin.readline

oelfinn = list(sorted([int(input()) for _ in range(int(input()))]))
for _ in range(int(input())):
    print(oelfinn[int(input()) - 1])