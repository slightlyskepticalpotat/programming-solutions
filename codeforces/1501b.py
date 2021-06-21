import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, drenched, least = int(input()), [int(i) for i in input().split()], [], float("inf")
    for i in range(n - 1, -1, -1):
        least = min(least, i - values[i] + 1) # bottommost drenched layer
        drenched.append(int(least <= i)) # check if current layer drenched
    print(*drenched[::-1])
