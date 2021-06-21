import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, unique, repeated = int(input()), [int(i) for i in input().split()], [], []
    for value in values:
        if value not in unique:
            unique.append(value)
        else:
            repeated.append(value)
    print(*sorted(unique) + repeated)
