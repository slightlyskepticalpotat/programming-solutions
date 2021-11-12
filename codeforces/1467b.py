import sys

input = sys.stdin.readline

def hill(x):
    if 0 < x < n - 1 and values[x - 1] < values[x] > values[x + 1]:
        return True
    return False

def valley(x):
    if 0 < x < n - 1 and values[x - 1] > values[x] < values[x + 1]:
        return True
    return False

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    extreme, inti = [0 for _ in range(n)], 0
    for i in range(1, n - 1):
        if hill(i) or valley(i):
            extreme[i] = 1
            inti += 1
    best = inti
    for i in range(1, n - 1):
        old = values[i]
        values[i] = values[i - 1]
        best = min(best, inti - extreme[i - 1] - extreme[i] - extreme[i + 1] + hill(i - 1) + valley(i - 1) + hill(i) + valley(i) + hill(i + 1) + valley(i + 1))
        values[i] = values[i + 1]
        best = min(best, inti - extreme[i - 1] - extreme[i] - extreme[i + 1] + hill(i - 1) + valley(i - 1) + hill(i) + valley(i) + hill(i + 1) + valley(i + 1))
        values[i] = old
    print(best)
