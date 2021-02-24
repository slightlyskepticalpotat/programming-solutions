import math

for _ in range(int(input())):
    n, values, real = int(input()), [int(i) for i in input().split()], []
    first, second = values[:n // 2 + 1], values[n // 2:][::-1]
    for i in range(n):
        if not i % 2:
            real.append(first.pop(0))
        else:
            real.append(second.pop(0))
    print(*real)
