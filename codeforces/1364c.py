import sys

input = sys.stdin.readline

n, a = int(input()), [int(i) for i in input().split()]
b = [-1 for _ in range(n)]
for i in range(1, n):
    if a[i] != a[i - 1]: # if it changes we added it
        b[i] = a[i - 1]
a, i = set(a), 0
for j in range(n):
    if b[j] == -1:
        while i in a: # lowest element not included
            i += 1
        b[j], i = i, i + 1
print(*b)
