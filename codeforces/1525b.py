import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if values == list(sorted(values)):
        print(0)
    elif values[0] == 1 or values[n - 1] == n:
        print(1)
    elif values[0] == n and values[n - 1] == 1:
        print(3)
    else:
        print(2)
