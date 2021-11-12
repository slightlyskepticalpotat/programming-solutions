import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = [i + 1 for i in range(int(input()))]
    if len(n) % 2:
        n[0], n[1], n[2] = 3, 1, 2
        for i in range(3, len(n), 2):
            n[i], n[i + 1] = n[i + 1], n[i]
    else:
        for i in range(0, len(n), 2):
            n[i], n[i + 1] = n[i + 1], n[i]
    print(*n)