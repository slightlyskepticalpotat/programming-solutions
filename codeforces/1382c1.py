import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b, k = int(input()), input().strip(), input().strip(), []
    for i in range(n):
        if a[i] != b[i]:
            k.append(i + 1)
            k.append(1)
            k.append(i + 1)
    print(len(k), *k)
    print()
