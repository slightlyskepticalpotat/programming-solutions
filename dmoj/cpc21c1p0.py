import sys

input = sys.stdin.readline

s = input().strip()
for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in s:
        print(char)
        break