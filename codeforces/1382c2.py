import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b, k1, k2 = int(input()), input().strip(), input().strip(), [], []
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            k1.append(i + 1)
    if a[n - 1] == "1":
        k1.append(n)
    for i in range(n - 1):
        if b[i] != b[i + 1]:
            k2.append(i + 1)
    if b[n - 1] == "1":
        k2.append(n)
    k = k1 + k2[::-1]
    print(len(k), *k)
