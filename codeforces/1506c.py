import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().strip(), input().strip()
    longest = 0
    for i in range(0, len(a) + 1):
        for j in range(i + 1, len(a) + 1):
            if a[i:j] in b:
                longest = max(longest, len(a[i:j]))
    print(len(a) + len(b) - longest * 2)
