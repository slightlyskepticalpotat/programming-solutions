import sys

input = sys.stdin.readline

n, values = int(input()), [int(i) for i in input().split()]
if n == 1:
    print(1, 1)
    print(-(values[0] + 2))
    print(1, 1)
    print(1)
    print(1, 1)
    print(1)
else:
    print(1, 1)
    print(-values[0])
    print(1, n)
    print(*([0] + [-n * values[i] for i in range(1, n)]))
    print(2, n)
    print(*[(n - 1) * values[i] for i in range(1, n)])
