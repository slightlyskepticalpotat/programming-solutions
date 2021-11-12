import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    if n - values.count(1) >= n / 2: # removing 1s
        print(n - values.count(1))
        print(*[0 for i in range(n - values.count(1))])
    else: # removing 0s
        print(values.count(1) - values.count(1) % 2)
        print(*[1 for i in range(values.count(1) - values.count(1) % 2)])
