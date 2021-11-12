import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(max(15, (int(input()) + 1) // 2 * 5))