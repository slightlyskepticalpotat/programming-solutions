import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(*[1 for i in range(int(input()))])
