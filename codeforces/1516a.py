import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    values, i = [int(i) for i in input().split()], 0
    while k and i != n - 1:
        if values[i] == 0:
            i += 1
            continue
        values[i] -= 1
        values[-1] += 1
        k -= 1
    print(*values)
