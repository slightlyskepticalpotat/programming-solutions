import sys
input = sys.stdin.readline
for i in range(5):
    stuff = [int(char) for char in input().strip()]
    print(max(stuff))